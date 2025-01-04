from multiprocessing import Process
import os
def func1(name):
    print(f"Hello {name}")
    # print("func进程id", os.getpid())
    # print("func父进程的id:demo.py的id", os.getppid())

if __name__ == '__main__':
    p1 = Process(target=func1, args = ("rzz",))
    p2 = Process(target=func1, args = ("www",))
    p3 = Process(target=func1, args = ("aaa",))
    # p4 = Process(target=func1, args = ("zzz",))
    # res = [p1,p2,p3,p4]
    # [i.start() for i in res]
    p1.daemon = True  #代表p为后台运行的守护进程，当p的父进程终止时，p也随之终止，并且设定为True后，p不能创建自己的新进程，必须在p.start()之前设置
    p1.start()
    p2.start()
    p3.start()
    # p2.join() #先进行子进程，在进行下面的程序
    # p1.join()

    print("我是主进程")
    # print("demo.py的进程id",os.getpid())
    # print("当前进程的父进程的id",os.getppid())

# class MyProcess(object):
#     def sing(self):
#         print("唱")
#     def dance(self):

#         print("跳")
# if __name__ == "__main__":
#     p1 = MyProcess()
#     s = Process(target=p1.sing)
#     d = Process(target=p1.dance)
#     s.start()
#     d.start()

