import numpy  as np
def F1():
    a=np.array([[1,2,3],[2,3,4]])
    print(a)
    dy=np.dtype('i4')
    b=np.array([[1,7,6],[897,9,6]],dtype=dy)
    print(b)
    print(b.shape)
    b.shape=(3,2)
    print(b)
    c=b.reshape(1,6)
    print(c)
def F2():
    a=np.zeros((5,),dtype=int) #零数组
    print(a)
    b=np.ones((5,),dtype=int)  #一数组
    print(b)
    c=np.full(shape=(4,4),fill_value=888) #×数值
    print(c)
    d=np.arange(1,78,step=3)  #从1到78 步长为3  起点、终点、步长
    print(d)
    print(np.linspace(2,66,10))     #从起始到结束  依据数量平均创建数组    起点、终点、数量
    print(np.random.randint(0,6))      #产生随机数，范围是（low，high）  产生的一定是整数
    print(np.random.random())      #产生随机数  范围是（0，1）  产生的是浮点数
    print(np.random.normal(0,1,10))   #正态分布（高斯分布）  输出符合此分布的10个数
def F3():
    x=np.zeros((25,25))
    for i in range(len(x)):
        for j in range(len(x[0])):
            if np.random.random()>=0.5:
                x[i][j]=255
    print(x)
if __name__ == '__main__':
    F3()