from controller.constants import Constants

class LCD:
    def __init__(self, controller, id):
        self.controller = controller
        self.id = id
        self.charId = chr(id + Constants.CHARACTER_OFFSET)

        # arduino-side initialization
        self.controller.writePacket('K' + self.charId + ';')

    def writeAt(self, text, x = 0, y = 0):
        xChar = chr(x + Constants.CHARACTER_OFFSET)
        yChar = chr(y + Constants.CHARACTER_OFFSET)
        self.controller.writePacket('B' + self.charId + xChar + yChar + ';')
        self.controller.writePacket('C' + self.charId + text + ';')

    def clear(self):
        self.controller.writePacket('D' + self.charId + ';')