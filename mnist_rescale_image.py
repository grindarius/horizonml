'''
a script to resize image to (160, 120) for mnist datasets, makes the train model reeally bad results
'''

from keras.datasets import mnist
import cv2
import numpy as np

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(x_train.shape)
print(x_train[0].shape)

def resize_image(old_image):
    return cv2.resize(old_image, (160, 120))

mapped_x_train = []
mapped_x_test = []

for image in x_train:
    mapped_x_train.append(resize_image(image))

for image in x_test:
    mapped_x_test.append(resize_image(image))

np.savez_compressed('./x_train.npz', x_train=np.array(mapped_x_train))
np.savez_compressed('./x_test.npz', x_test=np.array(mapped_x_test))
