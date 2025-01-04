# from greenlet import greenlet
# import time
#
# def fun1():
#     print("rzz")
#     # time.sleep(2)
#     g2.switch()
#     print("www")
# def fun2():
#     print("hello")
#     print("test")
#     g1.switch()
#
# g1 = greenlet(fun1)
# g2 = greenlet(fun2)
# g1.switch()

#一个线程中只能有一个携程
import gevent,time
from gevent import monkey
monkey.patch_all() #可以用time去切换

def drink(name):
    print(f"喝{name}")
    gevent.sleep(1) #只会识别自己认识的去切换
    print("我是函数一")
def eat(name):
    print(f"吃{name}")
    time.sleep(1)
    print("我是函数二")

g1 = gevent.spawn(drink,"七喜")
g2 = gevent.spawn(eat,"剁椒")
g1.join()
# g2.join()
