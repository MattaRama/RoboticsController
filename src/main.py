from controller.controller import Controller
from link.nethandler import NetHandler
import periodics

from controller.components.lcd import LCD
from controller.components.button import Button
from controller.components.led import LED
from controller.components.potentiometer import Potentiometer
from controller.components.rgbled import RGBLed

from time import sleep
import decimal
import math
import modules

# CONFIGURATION
USB_PORT = 'COM11'
MODULE_1 = modules.ALPHA
MODULE_2 = None
MODULE_2_DIG_OFFSET = 20,
MODULE_2_ANALOG_OFFSET = 7

# Controller initialization
c = Controller(USB_PORT)

module1IO = []
module2IO = []

def initModule(moduleType, slot):
    if moduleType == None:
        return
    
    # get IO array, pin numbers
    ioArr = module1IO if slot == 0 else module2IO

    for deviceConf in moduleType['devices']:
        if deviceConf['type'] == 'button':
            ioArr.append({
                'device': Button(c, deviceConf['pin']),
                'periodic': periodics.buttonPeriodic,
                'slot': slot,
                'name': deviceConf['name']
            })
        elif deviceConf['type'] == 'potentiometer':
            ioArr.append({
                'device': Potentiometer(c, deviceConf['pin'], 0, 1023),
                'periodic': periodics.potentiometerPeriodic,
                'slot': slot,
                'name': deviceConf['name']
            })
        elif deviceConf['type'] == 'led':
            ioArr.append({
                'device': LED(c, deviceConf['pin']),
                'periodic': periodics.ledPeriodic,
                'slot': slot,
                'name': deviceConf['name']
            })
        elif deviceConf['type'] == 'rgbled':
            ioArr.append({
                'device': RGBLed(c, deviceConf['pinR'], deviceConf['pinG'], deviceConf['pinB']),
                'periodic': periodics.rgbLEDPeriodic,
                'slot': slot,
                'name': deviceConf['name']
            })
        elif deviceConf['type'] == 'lcd':
            ioArr.append({
                'device': LCD(c, deviceConf['pin']),
                'periodic': periodics.lcdPeriodic,
                'slot': slot,
                'name': deviceConf['name']
            })

initModule(MODULE_1, 0)
initModule(MODULE_2, 1)

# NetHandler Initialization
nh = NetHandler(6868)
NH_INDICATOR_LIGHT = LED(c, 2)

# program loop
while True:
    NH_INDICATOR_LIGHT.setState(nh.inst.isConnected())
    
    for i in range(0, len(module1IO)):
        module1IO[i].periodic(module1IO[i].device, nh)
    for i in range(0, len(module2IO)):
        module2IO[i].periodic(module2IO[i].device, nh)