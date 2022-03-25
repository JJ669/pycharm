from pymouse import *
from pykeyboard import *
import time
m=PyMouse()
k=PyKeyboard()
x_dim,y_dim=m.screen_size()
print(x_dim,y_dim)

#m.click(x, y, button, n) x,y–坐标 button–（1为左键，2为右键），n–（默认1此，2表示双击，仅此两个值）




