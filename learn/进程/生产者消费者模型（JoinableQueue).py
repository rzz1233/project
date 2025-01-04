from multiprocessing import JoinableQueue, Process
import time
# 消费者不知道生产者有没有生产完,不知道生产了多少
# 生产者
def produce(q,name,produces):
    for i in range(2):
        # time.sleep(1)
        info = f"{name}的{produces}"
        q.put(info)
    q.join()
    # q.put(None)

# 消费者
def consume(q,name):
    while True:
        info = q.get()
        print(f"{name}买了{info}")
        q.task_done()

if __name__ == '__main__':
    q = JoinableQueue()
    p_pro1 = Process(target=produce,args=(q,"wyt","盐"))
    p_pro2 = Process(target=produce,args=(q,"zgy","油"))
    p_pro3 = Process(target=produce,args=(q,"zn","剁椒"))
    p_con1 = Process(target=consume,args=(q,"szx"))
    p_con2 = Process(target=consume,args=(q,"rzz"))
    p_con1.daemon = True
    p_con2.daemon = True

    [i.start() for i in [p_pro1,p_pro2,p_pro3,p_con1,p_con2]]
    p_pro1.join() #必须保证生产者全部生产完毕,才应该发送结束信号
    p_pro2.join()
    p_pro3.join()
    # q.put(None) #有几个消费者就应该发送几次结束信号None
    # q.put(None)