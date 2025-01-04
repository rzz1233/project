import sys
import socket
from threading import Thread
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget


class ServerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.initServer()

    def initUI(self):
        self.setWindowTitle('Chat Room Server')
        self.setGeometry(100, 100, 400, 400)

        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)

        self.clear_btn = QPushButton('Clear')
        self.clear_btn.clicked.connect(self.clearTextArea)

        layout = QVBoxLayout()
        layout.addWidget(self.text_area)
        layout.addWidget(self.clear_btn)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def initServer(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('192.168.111.37', 8088))
        self.server_socket.listen(5)

        self.text_area.append('Server started. Waiting for connections...\n')

        self.connections = []
        self.accept_connections()

    def accept_connections(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            self.connections.append(client_socket)
            self.text_area.append(f'Client connected: {client_address}')

            thread = Thread(target=self.handle_client, args=(client_socket,))
            thread.start()

    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if message:
                    self.text_area.append(f'Message from client: {message}')
                    self.broadcast(message, client_socket)
                else:
                    self.remove_connection(client_socket)
                    break
            except Exception as e:
                print(f'Exception: {e}')
                self.remove_connection(client_socket)
                break

    def broadcast(self, message, client_socket):
        for connection in self.connections:
            if connection != client_socket:
                try:
                    connection.send(message.encode('utf-8'))
                except Exception as e:
                    print(f'Exception: {e}')
                    self.remove_connection(connection)

    def remove_connection(self, client_socket):
        if client_socket in self.connections:
            self.connections.remove(client_socket)
            client_socket.close()

    def clearTextArea(self):
        self.text_area.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    server_window = ServerWindow()
    server_window.show()
    sys.exit(app.exec_())