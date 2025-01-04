import socket
import re
from multiprocessing import Process
class HTTP(object):
    def __init__(self,ip,port):
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_socket.bind((ip,port))
        self.tcp_socket.listen(127)
    def fun_socket(self,new_socket):
        buf = new_socket.recv(1024).decode("gbk")
        buf_split = buf.splitlines()[0]
        res = r"[^/]+(/[^ ]*)"
        result = re.match(res, buf_split).group(1)
        print(result)

        if result == "/":
            result = "/index.html"
        else:
            result = result
        try:
            with open( "web"+result, "r", encoding="utf-8") as f:
                con = f.read()
                msg = "HTTP/1.1 200 OK\n"
                msg += "\n"
                msg += con
                new_socket.send(msg.encode("utf-8"))
        except Exception as e:
            msg = "HTTP/1.1 404 NOT Found\n"
            msg += "\n"
            msg += "找不到页面"
            new_socket.send(msg.encode("gbk"))

    def run(self):
        while True:
            print("等待连接……")
            new_socket, client_addr = self.tcp_socket.accept()
            self.fun_socket(new_socket)

if __name__ == '__main__':
    http = HTTP("127.0.0.1",9091)
    p1 = Process(target=http.run)
    p1.start()
