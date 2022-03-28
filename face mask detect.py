 import cv2
>>> img = cv2.imread('C:/Users/HP/Pictures/ARNAB.png')
>>> img.shape
(768, 1366, 3)
>>> img[0]
array([[255, 255, 255],
       [255, 255, 255],
       [255, 255, 255],
       ...,
       [255, 255, 255],
       [255, 255, 255],
       [255, 255, 255]], dtype=uint8)
>>> import matplotlib.pyplot as plt
>>> plt.imshow(img)
<matplotlib.image.AxesImage object at 0x0000017D59571150>
>>> cv2.imshow('result',img)
>>> haar_data = cv2.CascadeClassifier('C:/Users/HP/AppData/Roaming/Python/Python310/site-packages/cv2/data/haarcascade_frontalface_default.xml')
>>> haar_data.detectMultiScale(img)
array([[614, 169, 214, 214],
       [792, 418,  86,  86],
       [402, 474,  73,  73]])
>>> # cv2.rectangle(img,(x,y),(w,h),(b,g,r),border_thickness)
>>> face = haar_data.detectMultiScale(img)
>>> for x,y,w,h in face:
...     cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,255), 4)
... cv2.imshow('result',img)
  File "<stdin>", line 3
    cv2.imshow('result',img)
    ^^^
SyntaxError: invalid syntax
