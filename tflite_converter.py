import tensorflow as tf
import pathlib

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

def generate_representative_data():
    for input_value in tf.data.Dataset.from_tensor_slices(x_train).batch(1).take(300):
        yield [input_value]

converter = tf.lite.TFLiteConverter.from_saved_model('./mnist_model_default_variables')
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.representative_dataset = generate_representative_data

# make conversion panics when it cannot convert to int
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.inference_input_type = tf.uint8
converter.inference_output_type = tf.uint8

tflite_model_quantized = converter.convert()

tflite_model_dir = pathlib.Path('mnist_tf_model_default_layers')
tflite_model_dir.mkdir(exist_ok=True, parents=True)

tflite_model_quantized_file = tflite_model_dir / 'mnist_model_quantized.tflite'
tflite_model_quantized_file.write_bytes(tflite_model_quantized)
