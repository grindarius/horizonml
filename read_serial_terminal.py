# https://stackoverflow.com/a/18115530
# https://youtu.be/AHr94RtMj1A

import serial
import signal
import sys
import datetime

data = []
start_time = datetime.datetime.now()

def signal_handler(signum, frame):
    logfile = open(
        f'./portenta_h7_log_{int(start_time.timestamp())}.txt', 'a+')
    logfile.write(
        f'log time: {start_time.isoformat()} to {datetime.datetime.now().isoformat()}\n')
    for line in data:
        logfile.write(line)

    logfile.close()
    sys.exit(0)

def main():
    port = serial.Serial('/dev/ttyACM0', 115200, timeout=0)
    start_time = datetime.datetime.now()

    while True:
        if port.in_waiting:
            packet = port.readline()
            decoded_string = packet.decode(
                encoding='utf-8', errors='ignore')
            decoded_string = datetime.datetime.now().isoformat() + ' ' + decoded_string
            data.append(decoded_string)

if __name__ == '__main__':
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, signal_handler)
    main()
