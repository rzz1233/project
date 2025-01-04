import socket
udp_sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_sk.bind(('192.168.111.24', 9998))
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
dic = {}
while True:
    msg, addr = udp_sk.recvfrom(1024) #接收msg, (ip,port)
    msg1 = msg.decode("utf-8")
    for i in user_dic:
        if i == addr[0]:
            dic[user_dic[i]] = addr
            print(f"{user_dic[i]}发来{msg1},ip是{i}")
            # print("客户端发来：",msg.decode("utf-8"))
    for i in dic:
        msg2 = addr[0] + "@" + msg1
        udp_sk.sendto(msg2.encode("utf-8"), dic[i])
    msg3 = input("请输入对客户端说的：")
    udp_sk.sendto(msg3.encode("utf-8"),addr)
    print("发送成功")
udp_sk.close()