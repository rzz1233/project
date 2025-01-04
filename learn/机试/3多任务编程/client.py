import socket
import threading


# 从服务器接收的消息
def receive(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if not message:
                break
            print(message)
        except:
            print("与服务器断开连接")
            client.close()
            break


# 向服务器发送消息
def send(client):
    while True:
        message = input("请输入要发送的信息：")
        client.send(message.encode('utf-8'))
        if message == "exit":
            client.close()
            break
        print("发送成功")


def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8088))

    t1= threading.Thread(target=receive, args=(client,))
    t2 = threading.Thread(target=send, args=(client,))

    t1.start()
    t2.start()


if __name__ == "__main__":
    start_client()
