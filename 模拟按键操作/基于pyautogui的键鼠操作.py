import pyautogui as pa
import pyperclip as pp
import time
import os
def f1():
    x_now,y_now=pa.position()
    pa.moveTo(600,16,duration=1)  #鼠标移动到目标位置
    pa.mouseDown()
    pa.moveTo(950,16,duration=1)
    pa.mouseUp()
    pa.click(1000,1400,button='left')  #鼠标在目标位置左键单击
    pa.moveTo(x_now,y_now,duration=1)

def f2():
    x_now,y_now=pa.position()
    pa.moveTo(600, 16, duration=1)
    pa.dragTo(950,16,duration=1)   #鼠标从当前位置拖动到目标位置
    pa.click(1000, 1400, button='left')
    pa.moveTo(x_now, y_now, duration=1)

def f3():
    x_now, y_now = pa.position()
    pa.click(600,500,button='left')
    pa.scroll(-1000)   #向上\下滚动多少单位
    pa.click(1000, 1400, button='left')
    pa.moveTo(x_now, y_now)

def f4():
    img=pa.screenshot()
    img.save('屏幕截图.jpg')

def f5():
    img=pa.screenshot()
    shoot=pa.locateOnScreen('2.bmp')
    print(shoot)
    pa.click(shoot[0],shoot[1])

def f6_1(dir):
    shoot1_name=dir+'11.png'
    shoot2_name=dir+'13.png'
    shoot3_name=dir+'14.png'
    shoot4_name=dir+'12.png'
    shoot_list=[shoot1_name,shoot2_name,shoot3_name,shoot4_name]  #杨俊轩  程云昊   郭佳鑫  张粟桐
    name1="杨俊轩"
    name2="程云昊"
    name3="郭佳鑫"
    name4="张粟桐"
    name=[name1,name2,name3,name4]
    max_y=0
    key=-10
    for i in range(0,4):
        if(pa.locateOnScreen(shoot_list[i], region=(1183,677,1404,774))!=None):
            shoot=pa.locateOnScreen(shoot_list[i],region=(1183,677,1404,774))
            print(type(shoot[1]),shoot[1])
            if(int(shoot[1])>max_y):
                max_y=shoot_list[i][1]
                key=i
    return name[key]
def f6(dir):
    shoot1=pa.locateOnScreen(dir+'1.bmp')
    pa.click(shoot1[0]+shoot1[2]/2,shoot1[1]+shoot1[3]/2)
    time.sleep(0.5)
    #if(pa.locateOnScreen(dir+'3.bmp')==None):
     #   shoot2=pa.locateOnScreen(dir+'2.bmp')
      #  pa.moveTo(shoot2[0]+shoot2[2]/2,shoot2[1]+shoot2[3]/2)
       # while(pa.locateOnScreen(dir+'3.bmp')==None):
        #    pa.scroll(-300)
         #   time.sleep(0.1)
    while(1):
        if(pa.locateOnScreen(dir+'3.bmp')!=None):
            shoot3=pa.locateOnScreen(dir+'3.bmp')
            pa.click(shoot3[0]+shoot3[2]/2,shoot3[1]+shoot3[3]/2)
            pa.press('shift')
            key=f6_1(dir)
            print(key)
            pp.copy(key+",您好！")
            pa.hotkey('ctrl','v')
            pa.press('enter')
            pa.press('shift')
            shoot4=pa.locateOnScreen(dir+'5.bmp')
            pa.click(shoot4[0]+shoot4[2]/2,shoot4[1]+shoot4[3]/2)

def f7():
    print(pa.position())
if __name__=='__main__':
    print(pa.size())
    x_window, y_window = pa.size()
    f6('C:\\Users\\huawei\\Desktop\\kk\\')



