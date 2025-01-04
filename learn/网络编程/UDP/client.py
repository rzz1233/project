import socket
udp_sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_port = ('192.168.111.24', 9998)
user_dic = {
    "192.168.111.38": "gxf",
    "192.168.111.20": "gzy",
    "192.168.111.24": "rzz",
    "192.168.111.52": "szy",
    "192.168.111.12": "zn",
    "192.168.111.35": "wyt",
    "192.168.111.25": "xj",
    "192.168.111.16": "宋波",
    "192.168.111.23": "lrp",
    "192.168.111.36": "bhx",
    "192.168.111.39": "lt",
    "192.168.111.22": "cj",
    "192.168.111.41": "lfl",
    "192.168.111.34": "rky",
    "192.168.111.42": "tmt",
    "192.168.111.31": "tr",
    "192.168.111.27": "by",
    "192.168.111.29": "cyq",
    "192.168.111.47": "yyh",
    "192.168.111.18": "wjh",
    "192.168.111.30": "lhz",
    "192.168.111.26": "jy",
    "192.168.111.13": "zy",
}
while True:
    msg1 =input("请输入对服务器说的：")
    udp_sk.sendto(msg1.encode("utf-8"),ip_port)
    msg, addr = udp_sk.recvfrom(1024)
    msg1 = msg.decode("utf-8")
    msg_lst = msg1.split("@", maxsplit=1)
    for i in user_dic:
        if i == msg_lst[0]:
            print(f'{user_dic[i]}说了{msg_lst[1]}')

    print("服务端发来：",msg.decode("utf-8"),addr)
