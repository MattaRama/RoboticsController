import ntcore
import time
from link.link_constants import LinkConstants
import logging

logging.basicConfig(level=logging.DEBUG)

class NetHandlerOptions:
    def __init__(self, teamNumber):
        self.teamNumber = teamNumber
        self.pushDelay = LinkConstants.DEFAULT_PUSH_DELAY
        self.devices = []

class NetHandler:
    def __init__(self, teamNumber, pushDelay = LinkConstants.DEFAULT_PUSH_DELAY):
        self.teamNumber = teamNumber
        self.__pushDelay__ = pushDelay
        
        # NT Setup
        self.inst = ntcore.NetworkTableInstance.getDefault()
        self.inst.startClient4('ExtraIO Controller')
        self.inst.setServerTeam(teamNumber)
        self.inst.startDSClient()

        # Table setup
        self.table = self.inst.getTable('ExtraIO')

#n = NetHandler(6868)
#table = n.inst.getTable('Shuffleboard')
#print(n.inst.isConnected())
#entry = table.getEntry('test')
#print(entry)
#entry.setString('bruh')