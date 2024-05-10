# from PIL import Image
# img=Image.open('./Picture/1126990.jpg')
# img.show()

# import cv2
# ID = "912336"
# image = cv2.imread('./Picture/{}.avif'.format(ID))
# cv2.imshow("image", image) # 显示图片，后面会讲解
# cv2.waitKey(0) #等待按键


# from PIL import Image
# import pillow_avif
# img = Image.open('./Picture/912336.avif')
# img.show()

from PIL import Image  # Pillow                    9.0.0
import pillow_avif  # pillow-avif-plugin        1.2.2

# 以上只是其中一个可用版本，并非必须
# 必须先安装pip install pillow-avif-plugin才能使用

AVIFfilename = './Picture/912336.avif'
AVIFimg = Image.open(AVIFfilename)
AVIFimg.save(AVIFfilename.replace("avif", 'jpg'), 'JPEG')
# 也可以是png等任意格式，但是转换的png有点大


# 反向，其他格式转AVIF
# JPGfilename = 'test.jpg'
# JPGimg = Image.open(JPGfilename)
# JPGimg.save(JPGfilename.replace("jpg", 'avif'), 'AVIF')
