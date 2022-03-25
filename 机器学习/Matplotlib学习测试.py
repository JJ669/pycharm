import math

import matplotlib.pyplot as plt
import numpy as np
def F1():   #分块画图
    fig=plt.figure()  #创建一个画布
    ax=fig.add_subplot(2,2,1)   #在画布上分成2✖2的块
    ax.set(xlim=[0,5],ylim=[-5,5],title='T1',xlabel='X',ylabel='Y')
    x=np.linspace(0,np.pi*30,99999)
    y1_sin=np.sin(x)
    y1_cos=np.cos(x)
    y1_e=np.exp(x)
    bx=fig.add_subplot(2,2,2)
    bx.set(xlim=[0,10],ylim=[-5,5],title='T2',xlabel='X',ylabel='Y')
    cx=fig.add_subplot(2,2,3)
    cx.set(xlim=[0,20],ylim=[0,100000],title='T3',xlabel='X',ylabel='Y')
    ax.plot(x,y1_sin,color='red',marker='+',label="y1")
    bx.plot(x,y1_cos,color='blue',label="y2")
    cx.plot(x,y1_e,color='black',label="y3")
    ax.legend(loc="upper left")
    bx.legend(loc="upper left")
    cx.legend(loc="upper left")
    plt.show()
def F2():     #折线图
    x=np.linspace(0,100,1000)
    y=np.sin(x)
    plt.plot(x,y,color='black',label="sin(x)")
    plt.legend(loc="upper left")
    plt.grid(color='red',linestyle="-")
    plt.axis([0,100,-2,2])
    plt.savefig('F2.jpg')
    plt.show()

def F3():   #散点图  matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, alpha=None, **kwargs)
    y=np.array([9,13,3,43,5,24,34,45,56,67,78,98,12,32,1])
    x=np.arange(0,len(y))
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('散点图')
    plt.scatter(x,y,s=10,c='red')  #s代表面积
    plt.show()
def F4():   #直方图   matplotlib.pyplot.bar（left，height，width = 0.8，bottom = None，hold = None，data = None，** kwargs ）还有color
    x=[1,2,3,4]
    y=[3,6,1,9]
    label=['red','yellow','black','blue']
    plt.xticks(x,label)  #将图中的x坐标替换为label
    plt.title('直方图')
    plt.ylabel('数量')
    plt.bar(x,y)
    plt.show()
def F5():    #饼图  matplotlib.pyplot.pie(x, explode=None, labels=None, colors=None, autopct=None, pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=None, radius=None, … )
    x=[1,2,3,4,5]
    labels=['red','yellow','black','blue','green']
    plt.pie(x,explode=[0.1,0.2,0.1,0.1,0.1],labels=labels,autopct='%.1f%%')
    plt.title('饼图')
    plt.show()
if __name__ =="__main__":
    #解决plt中文显示问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False