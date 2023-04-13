import ntcore
import logging
import time

logging.basicConfig(level=logging.DEBUG)

inst = ntcore.NetworkTableInstance.getDefault()
#table = inst.getTable('test')
#bruhSub = table.getBooleanTopic('bruh').subscribe(0)
#print(inst.isConnected()) 
inst.startClient4("test client")
inst.setServerTeam(6868)
inst.startDSClient()
#inst.setServer("localhost", ntcore.NetworkTableInstance.kDefaultPort4)
print(inst.isConnected())

while True:
    print(inst.isConnected())
    time.sleep(1)