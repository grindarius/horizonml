'''
this file is an example of converting a model to tflite in full int8 without any floats for
TPU machine and Edge devices.

code taken from https://www.tensorflow.org/lite/performance/post_training_integer_quant
'''
import tensorflow as tf
import numpy as np
import pathlib

# generating mnist model
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

def generate_representative_data():
    for input_value in tf.data.Dataset.from_tensor_slices(x_train).batch(1).take(100):
        yield [input_value]
        
x_train = x_train.astype(np.float32) / 255.0
x_test = x_test.astype(np.float32) / 255.0

# model = tf.keras.Sequential([
    # tf.keras.layers.InputLayer(input_size=(28, 28)),
    # tf.keras.layers.Reshape(target_shape=(28, 28, 1)),
    # tf.keras.layers.Conv2D(filters=12, kernel_size=(3, 3), activation='relu'),
    # tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    # tf.keras.layers.Flatten(),
    # tf.keras.layers.Dense(10)
# ])

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax),
])

print(model.summary())

model.compile(
    optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),
    metrics=['accuracy']
)

model.fit(
    x_train,
    y_train,
    epochs=5,
    validation_data=(x_test, y_test)
)

keras_model_converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = keras_model_converter.convert()

converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.representative_dataset = generate_representative_data

# make conversion panics when it cannot convert to int
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.inference_input_type = tf.uint8
converter.inference_output_type = tf.uint8

tflite_model_quantized = converter.convert()

tflite_model_dir = pathlib.Path('mnist_tf_model_default_layers')
tflite_model_dir.mkdir(exist_ok=True, parents=True)

tflite_model_file = tflite_model_dir / 'mnist_model.tflite'
tflite_model_file.write_bytes(tflite_model)

tflite_model_quantized_file = tflite_model_dir / 'mnist_model_quantized.tflite'
tflite_model_quantized_file.write_bytes(tflite_model_quantized)
