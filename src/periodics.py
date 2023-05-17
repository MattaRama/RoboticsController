def buttonPeriodic(buttonDevice, netHandler):
    entry = netHandler.inst.getTable('ExtraIO').getEntry(buttonDevice['name'])
    entry.setBoolean(buttonDevice.device.getValue())

def potentiometerPeriodic(potDevice, netHandler):
    entry = netHandler.inst.getTable('ExtraIO').getEntry(potDevice['name'])
    entry.setBoolean(potDevice.device.getValue())

def ledPeriodic(ledDevice, netHandler):
    entry = netHandler.inst.getTable('ExtraIO').getEntry(ledDevice['name'])
    entry.setDefaultBoolean(False)
    ledDevice.setState(entry.getBoolean())

def rgbLEDPeriodic(ledDevice, netHandler):
    table = netHandler.inst.getTable('ExtraIO').getTable(ledDevice['name'])
    red = table.getEntry('red')
    red.setDefaultNumber(0)
    green = table.getEntry('green')
    green.setDefaultNumber(0)
    blue = table.getEntry('blue')
    blue.setDefaultNumber(0)

    ledDevice.setRGBPWM(red.getNumber(), green.getNumber(), blue.getNumber())

def lcdPeriodic(lcdDevice, netHandler):
    table = netHandler.inst.getTable('ExtraIO').getTable(lcdDevice['name'])
    line1 = table.getEntry('line1')
    line2 = table.getEntry('line2')

    lcdDevice.writeAt(line1.getString(), 0, 0)
    lcdDevice.writeAt(line2.getString(), 0, 1)