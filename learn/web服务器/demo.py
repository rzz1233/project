import socket

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("127.0.0.1", 9090)
tcp_socket.bind(addr)
tcp_socket.listen(127)

while True:
    print("等待连接……")
    new_socket, client_addr = tcp_socket.accept()
    print(new_socket,addr)

    msg = "HTTP/1.1 200 OK\n"
    msg += "\n"
    msg += "<h1>任壮壮今天真帅</h1>"
    new_socket.send(msg.encode("gbk"))