import socket, json
from threading import Thread
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.connect(('127.0.0.1', 8085))  # 尝试连接服务器
def send():
    while True:
        se = input("请输入要发送的信息：")
        sk.send(se.encode('utf-8'))
        if se == "exit":
            sk.close()
            break
        print("发送成功")
def recv():
    while True:
        try:
            res1 = sk.recv(1024)
            res1 = res1.decode('utf-8')
            print(res1)
        except ConnectionAbortedError:
            break

if __name__ == '__main__':
    t1 = Thread(target=send)
    t2 = Thread(target=recv)
    t2.start()
    t1.start()

    t2.join()