from threading import Thread,Lock
import time
def say(name,l):
    l.acquire()
    time.sleep(1)
    print(f"{name}说你好")
    # print(time.time() - time1)
    l.release()

if __name__ == '__main__':
    L = Lock()
    time1 = time.time()
    t = Thread(target=say, args=("rzz",L))
    t.start()
    print("主程序")






# from threading import Thread
# import time
# class Sayhi(Thread):
#     def __init__(self,name):
#         super().__init__()
#         self.name=name
#     def run(self):
#         time.sleep(2)
#         print('%s say hello' % self.name)
#
# if __name__ == '__main__':
#     t = Sayhi('rose')
#     t.start()
#     print('主线程')