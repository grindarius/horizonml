import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model(
    './mnist_model_normalized'
)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()

with open('mnist_default.tflite', 'wb') as f:
    f.write(tflite_model)
