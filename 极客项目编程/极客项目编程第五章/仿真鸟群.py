import numpy as np
import pygame
import sys
import math
import time
def F1(B,i,R,N):   #减小两只小鸟重叠
    for j in range(N):
        if i != j:
            k1=abs(B[i].x-B[j].x)
            k2=abs(B[i].y-B[j].y)
            if k1*k1+k2*k2<R*R :
                return None
    return True
class brid(object):   #鸟类
    def __init__(self,x,y,screen,o,v,width,height):
        self.R=4
        self.r=1.5
        self.x=x
        self.y=y
        self.screen=screen
        self.o=o
        self.v=v
        self.width=width
        self.height=height
    def fly(self):   #画图
        self.x=self.x+self.v*math.cos(self.o)
        self.y=self.y-self.v*math.sin(self.o)
        pygame.draw.circle(self.screen,color='black',center=(self.x,self.y),radius=self.R,width=0)
        x_head=self.x+(self.R+self.r)*math.cos(self.o)
        y_head=self.y-(self.R+self.r)*math.sin(self.o)
        pygame.draw.circle(self.screen,color='black',center=(x_head,y_head),radius=self.r,width=0)
    def x_y(self):
        if self.x >width :
            self.x=0
        if self.x <0 :
            self.x=width
        if self.y > height:
            self.y=0
        if self.y <0 :
            self.y=height
    def go_mouse(self):
        x,y=pygame.mouse.get_pos()
        self.o=math.atan2((self.y-y),(x-self.x))
if __name__ == "__main__":
    pygame.init()
    width=1200
    height=600
    screen=pygame.display.set_mode((width,height))
    screen.fill(color='white')
    N=100
    B=[]
    for j in range(N):
        o_1=np.random.random()*2*math.pi
        x1=np.random.random()*width
        y1=np.random.random()*height
        v_1=np.random.randint(2,5)
        B_1=brid(x1,y1,screen,o_1,v_1,width,height)
        B.append(B_1)
    pygame.display.update()
    key = 1
    while(1):
        screen.fill(color='white')
        for i in range(N):
            if F1(B,i,B[i].R,N) and key==1:
                B[i].x_y()
                B[i].fly()
                B[i].go_mouse()
            else:
                B[i].x_y()
                B[i].fly()
        time.sleep(0.1)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()