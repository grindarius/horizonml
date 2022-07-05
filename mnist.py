'''
Hello world in Machine Learning made using MNIST datasets

code were from this tutorial: https://youtu.be/wQ8BIBpya2k
'''

from keras.datasets import mnist
import tensorflow as tf

# load data from the api (mnist dataset)
# 28x28 image of hand written digits 0-9
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# you can turn on these two lines and see for yourself whether them model works faster for
# normalized data or not
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

print(x_train.shape, y_train.shape)

print(x_train[0].shape)

model = tf.keras.models.Sequential()

# adding the input layer
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))

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

model.fit(x_train, y_train, epochs=5)

value_loss, value_accuracy = model.evaluate(x_test, y_test)
print(value_loss, value_accuracy)

model.save('mnist_model_normalized')
