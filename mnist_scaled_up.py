import cv2 
from keras.datasets import mnist
import numpy as np

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train_upsized_temp = []
x_test_upsized_temp = []

def resize_image(image):
    return cv2.resize(image, (160, 120))

for image in range(x_train.shape[0]):
    x_train_upsized_temp.append(resize_image(x_train[image]))

for image in range(x_test.shape[0]):
    x_test_upsized_temp.append(resize_image(x_test[image]))

x_train_upsized = np.array(x_train_upsized_temp)
x_test_upsized = np.array(x_test_upsized_temp)

print(x_train_upsized.shape)
