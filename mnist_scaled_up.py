'''
Trying out the model of mnist with an enlarged image size, and this does not go great.
'''
from keras.datasets import mnist
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

(_, y_train), (_, y_test) = mnist.load_data()

print('loading custom local data')
x_train_file = np.load('./x_train.npz', allow_pickle=True)
x_test_file = np.load('./x_test.npz', allow_pickle=True)

x_train = x_train_file['x_train']
x_test = x_test_file['x_test']

x_train_file.close()
x_test_file.close()

'''
Image normalization cannot be performed on the machine that I'm currently using in the lab,
because there's too little RAM for tensorflow to offload all the data into RAM to transform them.

I will try this on my own machine instead and hopefully generate a pre-normalized file and send
here using flash drive of some sort, the npz file is way too big to hold on github.
'''
print('normalizing images')
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

print(x_train.shape, x_test.shape)
print(x_train[0].shape)
print(x_test[0].shape)

plt.imshow(x_train[0])
plt.show()

print('creating model')
model = tf.keras.models.Sequential()

# adding the input layer
model.add(tf.keras.layers.Flatten(input_shape=(160, 120)))

# adding the hidden layer
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))

# adding the output layer
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

print(model.summary())

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

print('training model')
model.fit(x_train, y_train, epochs=5)

value_loss, value_accuracy = model.evaluate(x_test, y_test)
print(value_loss, value_accuracy)

model.save('mnist_model_scaled')
