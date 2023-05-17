import ntcore
import time
import logging
import link.nethandler
import controller.controller

# CONFIG
# System Config
UPDATE_LATENCY_SECS = 0.1

# IO Device IDs
CONNECTION_LED_ID = 7
LCD_1_INDEX = 0

# PROGRAM
logging.basicConfig(level=logging.DEBUG)

# Initialize Controller & networktables
control = controller.controller.Controller('COM11')
nethandler = link.nethandler.NetHandler(6868)
table = nethandler.table

# Initialize Controller Devices
connectionLed = control.getLED(CONNECTION_LED_ID) 
lcd1 = control.lcds[LCD_1_INDEX]
print('control init')

# Initialize Default Values
table.setDefaultString('lcdLine1', '')
table.setDefaultString('lcdLine2', '')
print('defaults init')

# Report loop
lcd1LastValues = ['', '']
print('report loop')
while True:
    # Connection LED
    connectionLed.setState(nethandler.inst.isConnected())

    # LCD Display
    lcd1Line1 = table.getString('lcdLine1', '')
    lcd1Line2 = table.getString('lcdLine2', '')
    if lcd1Line1 != lcd1LastValues[0]:
        lcd1.writeAt(' ' * 16, 0, 0)
        lcd1.writeAt(lcd1Line1, 0, 0)
        lcd1LastValues[0] = lcd1Line1
    if lcd1Line2 != lcd1LastValues[1]:
        lcd1.writeAt(' ' * 16, 0, 1)
        lcd1.writeAt(lcd1Line2, 0, 1)
        lcd1LastValues[1] = lcd1Line2

    time.sleep(UPDATE_LATENCY_SECS)