#事件
# 当使用set()时，是把is_set的bool值变为True
# 当使用clear()时，是把is_set的bool值变为False

# from multiprocessing import Event
# v = Event()
# print(v.is_set())
# v.set() # 可以让wait非阻塞
# v.clear() # 可以让wait阻塞
# v.set()
# v.wait()
# print("我是wait后的内容")

#信号灯模拟
from multiprocessing import Process,Event
import time
def deng(e):
    while True:
        if e.is_set():
            time.sleep(3)
            print("红灯")
            e.clear()
        else:
            time.sleep(2)
            print("绿灯")
            e.set()

def car(e,i):
    e.wait()
    print(f"通过第{i}辆车")

if __name__ == '__main__':
    e = Event()
    p = Process(target=deng,args=(e,))
    p.start()
    for i in range(100):
        cars = Process(target=car,args=(e,i))
        cars.start()
        time.sleep(1)