from controller.constants import Constants
import math

class LED:
    def __init__(self, controller, id):
        self.controller = controller
        self.id = id
        self.charId = chr(id + Constants.CHARACTER_OFFSET)
        controller.setPinMode(id, False)
    
    def setBrightnessPWM(self, pwm):
        pwmStr = str(pwm)
        for i in range(len(pwmStr) - 3):
            pwmStr = '0' + pwmStr
        self.controller.writePacket('H' + self.charId + pwmStr + ';')

    def setBrightnessPercent(self, percent):
        pwmVal = math.floor(percent * 255)
        self.setBrightnessPWM(pwmVal)

    def setState(self, high):
        self.controller.writePacket('G' + self.charId + ('1' if high else '0') + ';')