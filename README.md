# HorizonML
Machine Learning on the Edge of the Forest.

HorizonML is an undergraduate thesis project aiming to run a machine learning model directly on the board before shipping signals through [swarm](swarm.space).

## Requirements

You need
- [Arduino Portenta H7](https://store.arduino.cc/products/portenta-h7)
- [Arduino Portenta Vision Shield](https://store.arduino.cc/products/arduino-portenta-vision-shield-ethernet)
- [Arduino Uno](https://store.arduino.cc/arduino-uno-rev3)
- [OpenMV IDE](https://openmv.io/)
- [Arduino IDE](https://www.arduino.cc/en/software)

# Original setup
## Model setup
- Download [ECS-50](https://github.com/karolpiczak/ESC-50) dataset and [Urbansound8k](https://urbansounddataset.weebly.com/urbansound8k.html) dataset.
- Upload the data and the classes to Edge Impulse.
- Generate and export the model out as Arduino Library.

## Arduino setup
- Install Arduino cpp bootloader onto both boards.
- Sandwich the two Arduino boards together.
- Connect Rx/Tx pin from Portenta Vision Shield to Uno at port number 4 and 5 (Rx and Tx accordingly) of Portenta Vision Shield. Portenta H7's pin diagram [here](https://docs.arduino.cc/hardware/portenta-h7)
- Upload the code in file [portenta_h7.ino](./portenta_h7.ino) and [uno.ino](./uno.ino) onto the board accordingly.
- Run python script [read_serial_terminal.py](./read_serial_terminal.py) to capture any serial terminal activities.
- Download any sound you have associated with your class, and convert it to .mp3 format.
- Rename your sound file to the name you wanted to use and reference it in the file [testing.py](./testing.py)
- Run the file and wait for the sound to play.

# 2 Model OpenMV setup
## Model setup
- Train a simple image model on Edge Impulse, kinda like [this example](https://create.arduino.cc/projecthub/mjrobot/mug-or-not-mug-that-is-the-question-d4062a).
- Export the model as OpenMV Library.

## Arduino Setup
- Download OpenMV IDE
- Export the file from the above method onto the board's flash memory.
- Open the app and install MicroPython bootloader onto the board.
- Download `model.tflite` from [here](https://github.com/iabdalkader/microspeech-yesno-model).
- Put the downloaded file onto the flash memory of the board.
- Run the board with the code in the file [portenta_double_model.py](./portenta_double_model.py).
