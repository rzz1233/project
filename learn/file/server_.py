import socket
from threading import Thread

IP = '192.168.111.51'
PORT = 8080

user_dic = {
    "192.168.111.51": "gxf",
    "192.168.111.20": "gzy",
    "192.168.111.37": "rzz",
    "192.168.111.56": "szy",
    "192.168.111.55": "zn",
    "192.168.111.35": "wyt",
    "192.168.111.57": "xj",
    "192.168.111.50": "宋波",
    "192.168.111.29": "lrp",
    "192.168.111.21": "bhx",
    "192.168.111.39": "lt",
    "192.168.111.27": "cj",
    "192.168.111.41": "lfl",
    "192.168.111.34": "rky",
    "192.168.111.8": "tmt",
    "192.168.111.31": "tr",
    "192.168.111.24": "by",
    "192.168.111.59": "cyq",
    "192.168.111.52": "yyh",
    "192.168.111.18": "wjh",
    "192.168.111.30": "lhz",
    "192.168.111.26": "jy",
    "192.168.111.33": "zy",
}

def func(client_socket):
    while True:
        res = client_socket.recv(1024)
        # res = res.decode("utf-8")
        if res.decode("utf-8") == "exit":
            user_socket.remove(client_socket)
            client_socket.close()
            break
        for user in user_socket:
            user.send(res)
        print(f"{addr}说了{res.decode('utf-8')}")


if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen()

    user_socket = []

    while True:
        client_socket, addr = server_socket.accept()
        user_socket.append(client_socket)
        for user in user_socket:
            msg = f"欢迎{addr}光临"
            user.send(msg.encode("utf-8"))
        Thread(target=func,args=(client_socket,)).start()

