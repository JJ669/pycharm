import numpy as np
def way1(key1,key2):  #不换
    if key1 == key2:
        return 1
    else:
        return 0
def way2(key1,key2):   #换
    if key1 != key2:
        return 1
    else:
        return 0
def thrdoor():
    th=[1,1,1]  #初始化 1代表羊 0代表法拉利
    key1=np.random.randint(0,3)  #法拉利所在
    th[key1]=0
    key2=np.random.randint(0,3)   #所选
    key3=999
    for i in range(3):
        if th[i] == 1:
            if i == key2:
                True
            else:
                key3=i    #挑出的另一只羊
                break
    t1=way1(key1,key2)
    t2=way2(key1,key2)
    t=[t1,t2]
    return t
if __name__ =='__main__':
    times=100000
    t=[]
    t1=0
    t2=0
    for i in range(times):
        t=thrdoor()
        t1=t1+t[0]
        t2=t2+t[1]
    print(f'换获奖概率{float(t1/times)*100}%,不换获奖概率:{float(t2/times)*100}%')