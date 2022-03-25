import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
def F1():
    #x = np.array([[255, 0, 255,255,0,255,0], [255, 255, 0,255,0,255,0], [0, 255, 0,255,0,255,0],[255,0,255,0,255,0,255],[255,0,255,0,255,0,255]])
    color_value=255
    x=np.zeros((100,100))
    for i in range(len(x)):
        for j in range(len(x[0])):
            if np.random.random()>=0.5:
                x[i][j]=color_value
    max_x=len(x[0])
    max_y=len(x)
    while(1):
        y=x.copy()
        plt.imshow(x,interpolation='nearest')
        plt.draw()
        plt.pause(0.5)
        for i in range(max_y):
            for j in range(max_x):
                key=0
                if x[i][(j+1+max_x)%max_x] == color_value:
                    key=key+1
                if x[i][(j-1+max_x)%max_x] == color_value:
                    key=key+1
                if x[(i+1+max_y)%max_y][j] == color_value:
                    key=key+1
                if x[(i-1+max_y)%max_y][j] == color_value:
                    key=key+1
                if x[i][j]==color_value:
                    if key<2:
                        y[i][j] = 0
                    elif key==2 or key==3:
                        y[i][j] = color_value
                    elif key>3:
                        y[i][j] = 0
                elif x[i][j]==0:
                    if key==3:
                        y[i][j]=color_value
        x=y.copy()

if __name__ == '__main__':
    F1()