
import numpy as np
import cv2
from cv2 import *
import os
import random
import matplotlib.pyplot as plt
import pickle
from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D,Flatten,Dense
dataImage=[]
dir= r'C:\Users\lenovo\Desktop\dataAug\x2(1)'
categories=[]
for img in os.listdir(dir):
   newDir=dir+"/"+img
   ch=""
   k=0
   while img[k]!="-":
       ch=ch+img[k]
       k=k+1
   if ch not in categories:
       categories.append(ch)
   image=cv2.imread(newDir,1)
   try:
       image=cv2.resize(image,(30,30))
       dataImage.append([image,ch]) 
   except:
       print(img)
        
x=[]
y=[]
for features,labels in dataImage:
    x.append(features)
    y.append(categories.index(labels))
x=np.array(x)
y=np.array(y)
xtrain=[]
xtest=[]
ytrain=[]
ytest=[]

for i in range(len(x)):
    if i%73>=60 and i%20<=73:
        xtest.append(x[i])
        ytest.append(y[i])
    else:
        xtrain.append(x[i])
        ytrain.append(y[i])
xtest=np.array(xtest)        
ytest=np.array(ytest) 
xtrain=np.array(xtrain) 
ytrain=np.array(ytrain) 
model=Sequential()

model.add(Conv2D(64, (3,3), activation='relu',input_shape=(30,30,3)))
model.add(MaxPooling2D((2,2)))

model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPooling2D((2,2)))

model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPooling2D((2,2)))




model.add(Flatten())

model.add(Dense(256,activation= 'relu'))
model.add(Dense(70, activation='softmax'))
model.compile(optimizer= 'adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.fit(xtrain/255,ytrain,epochs=80,validation_split=0.05,shuffle=True)
score=model.evaluate(xtest/255,ytest)
print(score)
def test(n):
    image=cv2.imread('C:/Users/lenovo/Desktop/dataAug/x2/fish-6-x2r717.png',1)
    image=cv2.resize(image,(30,30))
    return model.predict(np.expand_dims(image, 0))


    
    
    
    
    
    