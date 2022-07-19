'''
https://www.tensorflow.org/lite/performance/post_training_integer_quant_16x8
'''

import logging
import tensorflow as tf
from tensorflow import keras
import numpy as np
import pathlib

input_shape = (28, 28)

logging.getLogger('tensorflow').setLevel(logging.DEBUG)

# check if 16x8 quantization mode is available
print(tf.lite.OpsSet.EXPERIMENTAL_TFLITE_BUILTINS_ACTIVATIONS_INT16_WEIGHTS_INT8)

# load MNIST dataset
mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# normalize inputs to between 0 and 1
x_train = x_train / 255.0
x_test = x_test / 255.0

print(x_train.shape)

model = keras.Sequential([
    keras.layers.InputLayer(input_shape=(28, 28)),
    keras.layers.Reshape(target_shape=(28, 28, 1)),
    keras.layers.Conv2D(filters=12, kernel_size=(3, 3), activation=tf.nn.relu),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),
    keras.layers.Flatten(),
    keras.layers.Dense(10),
    # keras.layers.Flatten(name='input_flatten_layer', input_shape=(28, 28)),
    # keras.layers.Dense(256, name='dense_hidden_layer', activation=tf.nn.relu),
    # keras.layers.Dense(10, name='output_layer', activation=tf.nn.softmax)
])

# model.build(input_shape)
print(model.summary())

model.compile(
    optimizer='adam',
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)

model.fit(
    x_train,
    y_train,
    epochs=5,
    validation_data=(x_test, y_test)
)

model.save('mnist_16x8')

tflite_models_dir = pathlib.Path('mnist_tflite-16x8')
tflite_models_dir.mkdir(exist_ok=True, parents=True)

converter = tf.lite.TFLiteConverter.from_saved_model('mnist_16x8')

converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.target_spec.supported_ops = [tf.lite.OpsSet.EXPERIMENTAL_TFLITE_BUILTINS_ACTIVATIONS_INT16_WEIGHTS_INT8]

images = tf.cast(x_train[0], tf.float32) / 255.0
mnist_dataset = tf.data.Dataset.from_tensor_slices((images)).batch(1)

def representative_data_gen():
    for input_value in mnist_dataset.take(100):
        yield [input_value]

converter.representative_dataset = representative_data_gen

tflite_16x8_model = converter.convert()
tflite_model_16x8_file = tflite_models_dir / 'mnist_model_quant_16x8.tflite'
tflite_model_16x8_file.write_bytes(tflite_16x8_model)
