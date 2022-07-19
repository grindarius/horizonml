'''
this file is continued from 'mnist.py' to test out the way tensorflow loads the model file and 
make predictions on them, so we can determine how to use it on the 'board' which is not the same
architecture and method calling like on the pc.

I discovered that the labels have to be added in later on, and have to correspond to the number
labels that our model uses, because model itself, as of my current knowledge, is not capable of
returning String labels.
'''

import tensorflow as tf
from keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt
import PIL

x_train_file = np.load('./x_train.npz')
x_test_file = np.load('./x_test.npz')

x_train = x_train_file['x_train']
x_test = x_test_file['x_test']

x_train_file.close()
x_test_file.close()

(_, y_train), (_, y_test) = mnist.load_data()

model = tf.keras.models.load_model('./mnist_model_scaled')

predictions = model.predict([x_test])

plt.figure(figsize=(10, 10))

for i in range(16):
    plt.subplot(4, 4, i + 1)
    img = x_test[i]
    plt.imshow(img)
    plt.title(y_test[i])
    plt.axis('off')

plt.show()

print(predictions[0])
print(np.argmax(predictions[0]))
