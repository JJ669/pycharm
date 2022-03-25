#随机生产灰度图片
from PIL import Image
import numpy as np
size=[1200,600]
np_1=np.zeros((size[1],size[0]),dtype=int)
for i in range(size[1]):
    for j in range(size[0]):
        np_1[i][j]=np.random.randint(0,255)
np_1_img=Image.fromarray(np_1)
print(np_1_img.size)
np_1_img.show()

