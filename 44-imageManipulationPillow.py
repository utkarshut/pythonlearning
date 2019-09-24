from PIL import Image , ImageFilter
import os
siz_300 = (300, 300)
image1 = Image.open('declaration.jpg')
#image1.rotate(90).save('dec.png')
#image1.convert(mode='L').save('dec.png')  # for bw
#image1.filter(ImageFilter.GaussianBlur(15)).save('dec.png')   #for blurring image

for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn, ftext = os.path.splitext(f)
        i.thumbnail(siz_300)
        i.rotate(90).save('pup.png')

#image1 = Image.open('declaration.jpg')
#image1.save('dec.png')
#image1.show()