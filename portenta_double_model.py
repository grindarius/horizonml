import sensor
import time
import tf
import uos
import gc
import micro_speech
import audio

audio_labels = ['Silence', 'Unknown', 'Yes', 'No']

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((96, 96))
sensor.skip_frames(time=2000)

audio_file = tf.load('/model.tflite')

speech = micro_speech.MicroSpeech()
audio.init(channels=1, frequency=16000, gain=24, highpass=0.9883)

audio.start_streaming(speech.audio_callback)

net = None
labels = None

try:
    # load the model, alloc the model file on the heap if we have at least 64K free after loading
    net = tf.load("trained.tflite", load_to_fb=uos.stat(
        'trained.tflite')[6] > (gc.mem_free() - (64*1024)))
except Exception as e:
    print(e)
    raise Exception(
        'Failed to load "trained.tflite", did you copy the .tflite and labels.txt file onto the mass-storage device? (' + str(e) + ')')

try:
    labels = [line.rstrip('\n') for line in open("labels.txt")]
except Exception as e:
    raise Exception(
        'Failed to load "labels.txt", did you copy the .tflite and labels.txt file onto the mass-storage device? (' + str(e) + ')')

clock = time.clock()
while (True):
    clock.tick()

    img = sensor.snapshot()

    for obj in net.classify(img, min_scale=1.0, scale_mul=0.8, x_overlap=0.5, y_overlap=0.5):
        print("**********\nPredictions at [x=%d,y=%d,w=%d,h=%d]" % obj.rect())
        # This combines the labels and confidence values into a list of tuples
        predictions_list = list(zip(labels, obj.output()))

        for i in range(len(predictions_list)):
            print("%s = %f" % (predictions_list[i][0], predictions_list[i][1]))

    idx = speech.listen(audio_file, timeout=3000,
                        threshold=0.78, filter=[2, 3])
    print(audio_labels[idx])

    print(clock.fps(), "fps")

audio.stop_streaming()
