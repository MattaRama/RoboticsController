from controller.constants import Constants
from controller.components.led import LED

class RGBLed:
    def __init__(self, controller, rId, gId, bId):
        self.controller = controller
        
        self.ledR = LED(controller, rId)
        self.ledG = LED(controller, gId)
        self.ledB = LED(controller, bId)

    def setRGBPWM(self, pwmR, pwmG, pwmB):
        self.ledR.setBrightnessPWM(pwmR)
        self.ledG.setBrightnessPWM(pwmG)
        self.ledB.setBrightnessPWM(pwmB)

    def setRGBPercent(self, r, g, b):
        self.ledR.setBrightnessPercent(r)
        self.ledG.setBrightnessPercent(g)
        self.ledB.setBrightnessPercent(b)