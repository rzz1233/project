import socket, json
from threading import Thread
ip = '127.0.0.1'
port = 8085
def func():
    while True:
        # print(f"连接成功：{addr}")
        res = conn.recv(1024)  # 接收客户端信息
        res1 = res.decode("utf-8")
        if res1 == "exit":
            user_socket.remove(conn)
            conn.close()
            break
        for user in user_socket:
            user.send(res)
        print(f"{addr}说了{res1}")

if __name__ == '__main__':
    sk = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, fileno=None)
    sk.bind((ip, port))  # 把地址绑定到套接字
    sk.listen()  # 监听链接
    print("服务器启动完成，等待连接")
    user_socket = []
    while True:
        conn, addr = sk.accept()  # 接受连接
        user_socket.append(conn)
        for user in user_socket:
            msg = f"欢迎{addr}光临"
            user.send(msg.encode("utf-8"))
        t = Thread(target=func)
        t.start()



