import socket
import re

# 解耦
def fun_socket(new_socket):
    buf = new_socket.recv(1024).decode("gbk")
    buf_split = buf.splitlines()[0]
    res = r"[^/]+(/[^ ]*)"
    result = re.match(res, buf_split).group(1)

    print(result)
    # print(buf_split)

    msg = "HTTP/1.1 200 OK\n"
    msg += "\n"
    msg += f"<h1>hello {result}</h1>"
    new_socket.send(msg.encode("gbk"))

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("127.0.0.1", 8080)
tcp_socket.bind(addr)
tcp_socket.listen(127)
while True:
    print("等待连接……")
    new_socket, client_addr = tcp_socket.accept()
    fun_socket(new_socket)

