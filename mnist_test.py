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

labels = ['who', 'can', 'see', 'the', 'better', 'picture', 'here', 'for', 'each', 'other']

(x_train, y_train), (x_test, y_test) = mnist.load_data()

model = tf.keras.models.load_model('./mnist_model.model')

predictions = model.predict([x_test])

print(predictions[0])
print(np.argmax(predictions[0]))
print(labels[np.argmax(predictions[0])])
