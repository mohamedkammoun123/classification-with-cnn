import numpy as np
import cv2
import os
import random
import matplotlib.pyplot as plt
import pickle
from PIL import Image
dir= r'C:/Users/lenovo/Desktop/original'
newDir=r'C:/Users/lenovo/Desktop/newData'
t=0
for img in os.listdir(dir):
    ch=str(img)
    ch1=""
    k=0
    
    if ch[-1]=="f" and ch[-2]=="i" and ch[-3]=="g" and ch!="confusions.eps":
        while ch[k]!=".":
            
            ch1=ch1+ch[k]
            
            k=k+1
        x=Image.open(dir+'/'+ch)
    
    x.save(newDir+"/"+ch1+".png")
    t=t+1
    print(t)
    

    