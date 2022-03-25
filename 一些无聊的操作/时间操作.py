import time
import pygame
import sys
import math
def F1(q,w,e,x,y,pos_second_x,pos_second_y,pos_minute_x,pos_minute_y,pos_hour_x,pos_hour_y,R):
    pygame.draw.circle(screen,color='black',center=(x,y),radius=R,width=2)
    for j in range(1,5*12+1): #60个小刻度
        o_small=math.pi/2-math.pi/30*j
        pos_line_x1=x+R*math.cos(o_small)
        pos_line_y1=y-R*math.sin(o_small)
        pos_line_x2=x+(R-5)*math.cos(o_small)
        pos_line_y2=y-(R-5)*math.sin(o_small)
        pygame.draw.line(screen,color='black',start_pos=(pos_line_x1,pos_line_y1),end_pos=(pos_line_x2,pos_line_y2),width=1)
    for i in range(1, 13):  # 12个大刻度  大刻度会覆盖小刻度
        text = text_init.render(f"{i}", True, "black", None)
        o_big = math.pi / 2 - math.pi / 6 * i
        pos_num_x = x - 5 + (R - 18) * math.cos(o_big)
        pos_num_y = y - 12 - (R - 18) * math.sin(o_big)
        screen.blit(text, (pos_num_x, pos_num_y))
        pos_line_x1 = x + R * math.cos(o_big)
        pos_line_y1 = y - R * math.sin(o_big)
        pos_line_x2 = x + (R - 10) * math.cos(o_big)
        pos_line_y2 = y - (R - 10) * math.sin(o_big)
        pygame.draw.line(screen, color='black', start_pos=(pos_line_x1, pos_line_y1),
                         end_pos=(pos_line_x2, pos_line_y2), width=3)
    pygame.draw.circle(screen,color='black',center=(x,y),radius=2,width=0)
    o_second=math.pi/2-2*math.pi/60*e
    pos_second_x=x+(R-35)*math.cos(o_second)
    pos_second_y=y-(R-35)*math.sin(o_second)
    o_minute=math.pi/2-2*math.pi/60*w
    pos_minute_x=x+(R-70)*math.cos(o_minute)
    pos_minute_y=y-(R-70)*math.sin(o_minute)
    o_hour=math.pi/2-2*math.pi/12*q
    pos_hour_x=x+(R-120)*math.cos(o_hour)
    pos_hour_y=y-(R-120)*math.sin(o_hour)
    pygame.draw.line(screen,color='black',start_pos=(x,y),end_pos=(pos_second_x,pos_second_y),width=3)
    pygame.draw.line(screen,color='black',start_pos=(x,y),end_pos=(pos_minute_x,pos_minute_y),width=6)
    pygame.draw.line(screen,color='black',start_pos=(x,y),end_pos=(pos_hour_x,pos_hour_y),width=10)

t=time.time()
pygame.init()
text_init=pygame.font.SysFont("隶书",20)
text1_init=pygame.font.SysFont("隶书",50)
screen=pygame.display.set_mode((1200,600))   #这就是一个surface
pygame.display.update()
screen.fill(color='white')
R_1=200  #圆的半径
x_1,y_1=600,300
pos_second1_x, pos_second1_y = x_1, y_1
pos_minute1_x, pos_minute1_y = x_1, y_1
pos_hour1_x, pos_hour1_y = x_1, y_1

R_2=50
x_2,y_2=400,300
now = time.localtime()
while(1):
    screen.fill(color='white')
    k=time.time()-t
    q,w,e=now[3],now[4],now[5]
    e=e+k
    w=w+k/60+now[5]/60
    q=q+k/3600+now[4]/60+now[5]/3600
    e_display=int(e)%60  #字体显示 秒
    w_display=int(w)%60  #字体显示 分
    q_display=int(q)%24  #字体显示 时
    e=int(e) #秒  second
    text1=text1_init.render(f"{q_display}:{w_display}:{e_display}",True,'black',None)
    screen.blit(text1,(x_1-80,y_1-260))
    F1(q,w,e,x_1,y_1,pos_second1_x,pos_second1_y,pos_minute1_x,pos_minute1_y,pos_hour1_x,pos_hour1_y,R_1)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
