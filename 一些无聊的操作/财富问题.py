import random
import matplotlib.pyplot as plt
import numpy as np
def F1(): #不排序
    man_list=[]
    for i in range(100):
        man_list.append(100)
    fig = plt.figure()  # 创建一个画布
    for j in range(1000,17000,500):
        for i in range(j): #j是游戏轮次
            for man1 in range(100):
                man2=random.randint(0,99)
                if man_list[man1]>0:  #防止欠款
                    man_list[man1]=man_list[man1]-1
                    man_list[man2]=man_list[man2]+1
        x=np.linspace(1,100,100)
        plt.title(f'Round:{j}')
        plt.ylabel('money')
        plt.bar(x, man_list)
        plt.draw()
        plt.pause(0.1)
        plt.cla()
def F2(): #排序
    man_list=[]
    for i in range(100):
        man_list.append(100)
    fig = plt.figure()  # 创建一个画布
    for j in range(1000,17000,500):
        for i in range(j):  # j是游戏轮次
            for man1 in range(100):
                man2 = random.randint(0, 99)
                if man_list[man1] > 0:
                    man_list[man1] = man_list[man1] - 1
                    man_list[man2] = man_list[man2] + 1
        x = np.linspace(1, 100, 100)
        for p in range(99):
            for q in range(99-p):
                if man_list[q]>man_list[q+1]:
                    t=man_list[q]
                    man_list[q]=man_list[q+1]
                    man_list[q+1]=t
        plt.title(f'Round:{j}')
        plt.ylabel('money')
        plt.bar(x,man_list)
        plt.draw()
        plt.pause(0.1)
        plt.cla()
def F3(): #可负债
    man_list = []
    for i in range(100):
        man_list.append(100)
    fig = plt.figure()  # 创建一个画布
    for j in range(1000,17000,500):
        for i in range(j):  # j是游戏轮次
            for man1 in range(100):
                man2 = random.randint(0, 99)
                man_list[man1] = man_list[man1] - 1
                man_list[man2] = man_list[man2] + 1
        x = np.linspace(1, 100, 100)
        for p in range(99):
            for q in range(99 - p):
                if man_list[q] > man_list[q + 1]:
                    t = man_list[q]
                    man_list[q] = man_list[q + 1]
                    man_list[q + 1] = t
        plt.title(f'Round:{j}')
        plt.ylabel('money')
        plt.bar(x, man_list)
        plt.draw()
        plt.pause(0.1)
        plt.cla()
if __name__ == '__main__':
    F2()