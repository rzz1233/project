import sys
import socket
from threading import Thread
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QLineEdit


class ClientWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.initClient()

    def initUI(self):
        self.setWindowTitle('Chat Room Client')
        self.setGeometry(100, 100, 400, 400)

        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)

        self.message_input = QLineEdit()
        self.send_btn = QPushButton('Send')
        self.send_btn.clicked.connect(self.sendMessage)

        layout = QVBoxLayout()
        layout.addWidget(self.text_area)
        layout.addWidget(self.message_input)
        layout.addWidget(self.send_btn)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def initClient(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('192.168.111.37', 8088))

        thread = Thread(target=self.receiveMessages)
        thread.start()

    def receiveMessages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    self.text_area.append(message)
            except Exception as e:
                print(f'Exception: {e}')
                self.client_socket.close()
                break

    def sendMessage(self):
        message = self.message_input.text()
        if message:
            self.client_socket.send(message.encode('utf-8'))
            self.message_input.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    client_window = ClientWindow()
    client_window.show()
    sys.exit(app.exec_())