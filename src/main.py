import ntcore
import time
import logging
import link.nethandler
import controller.controller

# CONFIG
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

# Initialize Default Values
table.setDefaultString('lcdLine1', '')
table.setDefaultString('lcdLine2', '')

# Report loop
lcd1LastValues = ['', '']
while True:
    # Connection LED
    connectionLed.setState(nethandler.inst.isConnected())

    # LCD Display
    lcd1Line1 = table.getString('lcdLine1', '')
    lcd1Line2 = table.getString('lcdLine2', '')
    if len(lcd1Line1) > 0 and lcd1Line1 != lcd1LastValues[0]:
        lcd1.writeAt(' ' * 16, 0, 0)
        lcd1.writeAt(lcd1Line1, 0, 0)
        lcd1LastValues[0] = lcd1Line1
    if len(lcd1Line2) > 0 and lcd1Line2 != lcd1LastValues[1]:
        lcd1.writeAt(' ' * 16, 0, 1)
        lcd1.writeAt(lcd1Line2, 0, 1)
        lcd1LastValues[1] = lcd1Line2