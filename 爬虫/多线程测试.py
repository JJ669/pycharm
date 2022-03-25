import threading
import time
def f1(k):
    print(f"程序: {k}")
    print("123456789")
    print("1+2=?")
    print("3")
    time.sleep(1)
    print(f"{k}程序结束")

if __name__ == '__main__':
    start_1=time.time()
    f1(2)
    end_1=time.time()
    pp=end_1-start_1
    print(f'单线程花费时间为：{pp}')
    start_2=time.time()
    t1=threading.Thread(target=f1,args=(3,))   #设置多线程
    t2=threading.Thread(target=f1,args=(4,))   #设置多线程
    t1.setDaemon(True)   #设置为守护线程
    t2.setDaemon(True)   #设置为守护线程
    t1.start()
    t2.start()
    end_2=time.time()
    tt=end_2-start_2
    print(f'双线程花费时间为：{tt}')