import socket,re
import time

socket_lst = []

def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ("127.0.0.1", 9090)
    tcp_socket.bind(addr)
    tcp_socket.listen(127)

    tcp_socket.setblocking(False)

    while True:
        time.sleep(1)
        print("等待连接……")
        try:
            new_socket = tcp_socket.accept()
        except Exception as e:
            print("没有客户端连接")

        else:
            print("有一个客户端连接")
            new_socket[0].setblocking(False)
            socket_lst.append(new_socket)

        for client_socket,addr in socket_lst:
            try:
                buf = client_socket.recv(1024).decode("gbk")
                print(buf)

                if buf:
                    print("接收到的消息是：", buf)

                else:
                    print(f"{client_socket} 被关闭了")
                    client_socket.close()
                    socket_lst.remove((client_socket,addr))
            except:
                pass

if __name__ == '__main__':
    main()