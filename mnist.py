from keras.datasets import mnist

# * load data from the api (mnist datasetl)
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(x_train.shape, y_train.shape)
