from operationData import translation,centreRotation,convertToRadius,ImageToClasse
import os
import cv2
import numpy as np
import math
dataImage=[]
dir=r'C:/Users/lenovo/Desktop/newData'
dir1=r'C:/Users/lenovo/Desktop/dataAug/x2(1)'
k=0
for img in os.listdir(dir):
    k=k+1
    if k>=0:
        newDir=dir+"/"+img
        image=cv2.imread(newDir,2)
        image=cv2.resize(image,(250,250))
        dataImage.append(image)
        k=k+1
        for i in range(2,3):
           phi=convertToRadius(2*math.pi/i)
           try:
               rotImage=centreRotation(image,phi)
           
               rotImage1=centreRotation(image, phi)
           except:
               print(phi)
           
            
           cv2.imwrite(dir1+'/'+ImageToClasse(img)+'-x4t'+str(k)+str(i)+'.png',rotImage)
           
           cv2.imwrite(dir1+'/'+ImageToClasse(img)+'-x4t1'+str(k)+str(i)+'.png',rotImage1) 
    else:
         print(k)





        





