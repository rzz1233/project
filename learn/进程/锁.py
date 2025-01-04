# import os
# import time
# import random
# from multiprocessing import Process
#
# def work(n):
#     print('%s: %s is running' % (n, os.getpid()))
#     time.sleep(random.random())
#     print('%s: %s is done' % (n, os.getpid()))
#
#
# if __name__ == '__main__':
#     for i in range(3):
#         p = Process(target=work, args=(i,))
#         p.start()

#加锁
import os
import time
import random
from multiprocessing import Process,Lock
# 加锁后按顺序执行
def work(lock,n):
    lock.acquire()
    print('%s: %s is running' % (n, os.getpid()))
    time.sleep(random.random())
    print('%s: %s is done' % (n, os.getpid()))
    lock.release()

if __name__ == '__main__':
    lock=Lock()
    for i in range(3):
        p=Process(target=work,args=(lock,i))
        p.start()

# 信号量：一把锁配多把钥匙
# from multiprocessing import Semaphore
#
# l = Semaphore(3) #可以开3把锁
# l.acquire()
# print(111)
# l.acquire()
# print(222)
# l.acquire()
# print(333)
# # l.release()  #加上他就不用钥匙，它本身可以开锁
# l.acquire()
# print(44)


