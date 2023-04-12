from controller.constants import Constants

class Potentiometer:
    def __init__(self, controller, id, min, max):
        self.controller = controller
        self.id = id
        self.charId = chr(id + Constants.CHARACTER_OFFSET)
        self.min = min
        self.max = max

    # returns a value between 0 and 1023
    def getValue(self):
        self.controller.writePacket('E' + self.charId + ';')
        packet = self.controller.readPacket()
        return int(packet[1:len(packet) - 1])

    # gets the potentiometer percent, between 0 and 1
    def getPercent(self):
        rawVal = self.getValue()
        return (rawVal - self.min) / (self.max - self.min)