import cv2 
from keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np

(x_train, y_train), (x_test, y_test) = mnist.load_data()

def f(x):
    return cv2.resize(x, (160, 120))

x_train = f(x_train)
x_test = f(x_test)

print(x_train.shape)

# plt.imshow(x_train[0])
# plt.show()

# resized = cv2.resize(x_train[0], (160, 120))
# plt.imshow(resized)
# plt.show()
