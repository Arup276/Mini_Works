# dependencies
from keras import models
from keras.datasets import mnist
from keras.layers import Flatten,Dense
import tensorflow as tf
import numpy as np
import cv2
import matplotlib.pyplot as plt
#%matplotlib inline

# dataset
(x_trai,y_train),(x_tes,y_test) = mnist.load_data()

# normalize the dataset
x_train = tf.keras.utils.normalize(x_trai,axis = 1)
x_test = tf.keras.utils.normalize(x_tes,axis = 1)

model = models.Sequential()

model.add(Flatten()) # to pass the 28x28 size input in | form
model.add(Dense(units = 128,activation = 'relu'))
model.add(Dense(units = 128,activation = 'relu'))
model.add(Dense(units = 10,activation = 'sigmoid'))

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

model.fit(x_train,y_train,epochs = 3 ,batch_size = 16)

val_loss,val_acc = model.evaluate(x_test,y_test)


print(val_loss,val_acc)

while True:
    #quit = input("To quit press ['q']: ")
    inp = input("Enter any img number from test set or to eixt['q']: ")
    if inp == 'q':
        break
    else:
        n = int(inp)
        img = x_test[n]
        pred = model.predict([[x_test[n]]])
        num = np.argmax(pred)
        num = str(num)
        print(num)
        img2 = cv2.putText(img,num,(5,5),cv2.FONT_HERSHEY_COMPLEX,1, (255 ,0 ,0), 0.2) # putting the label on the topleft corner
        cv2.imshow(img2) # cmap = plt.cm.binary
        cv2.show()
