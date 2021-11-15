import time
import pickle
from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D,Flatten,Dense
from keras.callbacks import TensorBoard

Name= 'cat-vs-dog-prediction'

tensorBoard=TensorBoard(log_dir=r'C:/Users/lenovo/Desktop/datar')

x=pickle.load(open('x.pkl','rb'))
y=pickle.load(open('y.pkl','rb'))
x=x/255

model=Sequential()

model.add(Conv2D(64, (3,3), activation='relu',input_shape=(30,30,3)))
model.add(MaxPooling2D((2,2)))

model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPooling2D((2,2)))

model.add(Flatten())

model.add(Dense(128,activation= 'relu'))
model.add(Dense(2, activation='softmax'))
model.compile(optimizer= 'adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.fit(x,y,epochs=5,validation_split=0.1,callbacks=[tensorBoard])