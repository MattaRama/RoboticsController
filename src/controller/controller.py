import serial
import time
from controller.components.lcd import LCD
from controller.components.button import Button
from controller.components.led import LED
from controller.components.potentiometer import Potentiometer
from controller.components.rgbled import RGBLed

class Controller:
    def __init__(self, port):
        # establish arduino 
        self.arduino = serial.Serial(port=port, baudrate=9600, timeout=.1)
        self.lcds = []

        # wait for connection to be verified
        packet = self.readPacket()
        if (packet != 'Begin;'):
            raise Exception('First Arduino packet was not "Begin;"')

        # get inits
        packet = ''
        while (packet := self.readPacket()) != 'Init;':
            # LCD inits
            if (packet.startswith('LCDInit ')):
                idRaw = packet.split(' ')[1]
                id = idRaw[:len(idRaw) - 1]
                self.lcds.append(LCD(self, int(id)))

    # read packet is blocking
    def readPacket(self):
        ret = ''
        while True:
            while self.arduino.inWaiting() <= 0:
                time.sleep(0.05)
            char = self.arduino.read().decode('utf-8')
            ret += char
            if char == ';':
                break
        return ret

    # writes data to serial out
    def writePacket(self, data):
        self.arduino.write(bytes(data, 'ascii'))

    def getButton(self, pin):
        return Button(self, pin)

    def getLED(self, pin):
        return LED(self, pin)

    def gePotentiometer(self, pin, min = 0, max = 1023):
        return Potentiometer(self, pin, min, max)

    def getRGBLed(self, rPin, gPin, bPin):
        return RGBLed(self, rPin, gPin, bPin)