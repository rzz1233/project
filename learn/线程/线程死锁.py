from threading import Thread, Lock, RLock
def man(name,l_wc,l_zhi):
    l_zhi.acquire()
    print(f"{name}拿到了纸")
    l_wc.acquire()
    print(f"{name}在厕所")
    l_zhi.release()
    l_wc.release()

def woman(name,l_wc,l_zhi):
    l_wc.acquire()
    print(f"{name}在厕所")
    l_zhi.acquire()
    print(f"{name}拿到了纸")
    l_zhi.release()
    l_wc.release()

if __name__ == '__main__':
    l_wc = l_zhi = Lock() #解决死锁的方法将lock（）变为Rlock()
    t1 = Thread(target=man, args=("rzz",l_wc,l_zhi))
    t2 = Thread(target=woman, args=("www",l_wc,l_zhi))
    t1.start()
    t2.start()
