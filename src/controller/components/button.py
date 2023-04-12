from controller.constants import Constants

class Button:
    def __init__(self, controller, pinId):
        self.controller = controller
        self.pinId = pinId
        self.pinChar = chr(pinId + Constants.CHARACTER_OFFSET)

    def getValue(self):
        self.controller.writePacket('F' + self.pinChar + ';')
        packet = self.controller.readPacket()
        val = packet[1]
        return True if val == '1' else False