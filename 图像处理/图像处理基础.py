from PIL import Image
import numpy as np
dog=Image.open("宠物.png")
print(dog.mode,dog.size,dog.format)
dog_2=dog.convert('L')  #通过该方法你可以将PIL图像转换成九种不同的格式，分别1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。
#r,b,g=dog.split()  #分3个通道
#dog_3=Image.merge('RGB',(r,b,g))
#box=(300,400,600,600)
#region=dog.crop(box)  #剪切
#region=region.transpose(Image.ROTATE_180)    #旋转
#dog_1=dog.copy()   #复制
#dog_1.paste(region,box)#粘贴
dog_np=np.array(dog_2)  #图片大小（X,Y)转换为数组有三（二）个维度，彩色图片最小维度由[R,G,B]组成（灰色图片最小维度由每个像素点值组成)，相当于每一个像素点，
# 最小维度有X个相当于图片的横轴像素点X个，有Y个由X个最小维度组成的数组相当于图片的纵轴像素点Y个
value=100
#像素点越接近0越黑，越接近255越白
for i in range(len(dog_np)):
    for j in range(len(dog_np[0])):
        if dog_np[i][j]-value<=0:
            dog_np[i][j]=0
        else:
            dog_np[i][j]=dog_np[i][j]-value
dog_np_img=Image.fromarray(dog_np)  #从数组还原图片
dog_np_img.show()
dog_2.show()