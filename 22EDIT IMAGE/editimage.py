#installation of pillow library
#change the image extension
# resize image file
#resize multiple image using for loop
#sharpness
# colour
#contrast
#image blur,gaussianBlur
# from distutils import extension 
# import os
from re import I
from PIL import Image,ImageEnhance,ImageFilter
# img1=Image.open('dog1.jpg')

### save file in , pdf, png, and other
# img1.save('dog1.png')# file save in png file
# img1.save('dog1.pdf')# file save in pdf file

### only show dont show in pdf, jpg, png
# img2=Image.open('dog2.jpg')
# img2.show()

### image file resize
# max_size=(350,350)
# img1.thumbnail(max_size)
# img1.save('dog1small.jpg')
# for item in os.listdir():
#         if item.endswith('.jpg'):
#                 img1=Image.open(item) 
#                 filename,extension=os.path.splitext(item)
#                 img1.save(f'{filename}.png')

### sharpness, color, contrast,
#sharpness
# img1=Image.open('dog1.jpg')
# enh=ImageEnhance.Sharpness(img1)
# enh.enhance(5).save('dog11.jpg')
####color
# img1=Image.open('dog1.jpg')
# enh=ImageEnhance.Color(img1)
# enh.enhance(2).save('dog11.jpg')

# ###brightness
# img1=Image.open('dog1.jpg')
# enh=ImageEnhance.Brightness(img1)
# enh.enhance(1.1).save('dog11.jpg')

# ###contrast
# img1=Image.open('dog1.jpg')
# enh=ImageEnhance.Contrast(img1)
# enh.enhance(1).save('dog11.jpg')


### image blur
img1=Image.open('dog1.jpg')
img1.filter(ImageFilter.GaussianBlur(radius=4)).save('dog11.jpg')
