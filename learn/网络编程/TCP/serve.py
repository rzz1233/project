# import socket, json
# sk = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM,proto=0,fileno=None)
# sk.bind(('127.0.0.1',8080))  #把地址绑定到套接字
# sk.listen()  #监听链接
# conn,addr = sk.accept()  #接受连接
# res = conn.recv(1024)  #接收客户端信息
# print(res)
# msg = [123,'ss']
# mgs1 = json.dumps(msg)
# conn.send(mgs1.encode('utf-8'))#向客户端发送信息
# conn.close()
# sk.close()  #关闭套接字

import socket, json
sk = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM,proto=0,fileno=None)
sk.bind(('127.0.0.1', 8080))  # 把地址绑定到套接字
sk.listen()  # 监听链接
print("服务器启动完成，等待连接")
conn, addr = sk.accept()  # 接受连接
print(conn)
while True:

    print(f"连接成功：{addr}")
    res = conn.recv(1024)  # 接收客户端信息
    res1 = res.decode("utf-8")
    print("客户端说了：",res1)

    se = input("请输入对客户端说的：")
    conn.send(se.encode('utf-8'))#向客户端发送信息
    print("发送完成")

sk.close()  #关闭套接字