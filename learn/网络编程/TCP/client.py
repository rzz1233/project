# import socket, json
# sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sk.connect(('127.0.0.1',8080)) # 尝试连接服务器
# sk.send(b"hisss")
#
# res = sk.recv(1024)  # 对话(发送/接收)
# res1 = res.decode("utf-8")
# res1 = json.loads(res1)
# print(res1)
#
# sk.close()


import socket, json
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.connect(('127.0.0.1', 8080))  # 尝试连接服务器
while True:
    se = input("请输入：")
    sk.send(se.encode('utf-8'))
    print("输入成功")

    res1 = sk.recv(1024)
    res1 = res1.decode('utf-8')
    print("服务器说了：",res1)
sk.close()