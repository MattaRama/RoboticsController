import serial
import time
from threading import Thread

arduino = serial.Serial(port='COM10', baudrate=9600, timeout=.1)

def write(data):
    arduino.write(bytes(data, 'utf-8'))

def read():
    ret = ''
    while True:
        while arduino.inWaiting() <= 0:
            time.sleep(0.05)
        char = arduino.read().decode('utf-8')
        ret += char
        if char == ';':
            break
    return ret

def readLoop():
    while True:
        ret = ''
        while True:
            while arduino.inWaiting() <= 0:
                time.sleep(0.05)
            char = arduino.read().decode('utf-8')
            ret += char
            if char == ';':
                break
        print(ret)

# read thread
readThread = Thread(target=readLoop, name='readThread0')
readThread.start()

# write thread
print('Connection Opened')
while True:
    try:
        text = input('')
        write(text)
    except:
        exit(-1)
