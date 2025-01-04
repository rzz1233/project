import socket
from threading import Thread


# 处理客户端连接
def handle_client(client_socket, addr):
    print(f"新连接：{addr}")
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"{addr} 说: {message}")

            send_client(message, client_socket)
        except:
            client_socket.close()
            break


def send_client(message, client_socket):
    for client in clients:
        if client != client_socket:
            client.send(message.encode('utf-8'))

# 初始化服务端
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8088))
    server.listen()
    print("服务器启动，等待连接")

    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)

        t1 = Thread(target=handle_client, args=(client_socket, addr))
        t1.start()

if __name__ == "__main__":
    clients = []
    main()
