from controller.controller import Controller
from link.nethandler import NetHandler
from time import sleep
import decimal
import math

c = Controller('COM11')

net = NetHandler(6868)
testTable = net.inst.getTable('test')

pot = c.gePotentiometer(0, 0, 1023)
lcd = c.lcds[0]
led = c.getLED(3)
while True:
    val = pot.getValue()
    percent = round(pot.getPercent(), 5)
    print(f'{val} : {percent}')
    lcd.clear()
    lcd.writeAt(str(percent), 0, 0)
    led.setBrightnessPercent(percent)
    testTable.getEntry('testVal').setValue(percent)