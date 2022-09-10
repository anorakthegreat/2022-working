import threading
from networktables import NetworkTables, NetworkTablesInstance

cond = threading.Condition()
notified = [False]

def connectionListener(connected, info):
    print(info, '; Connected=%s' % connected)
    with cond:
        notified[0] = True
        cond.notify()

NetworkTables.initialize(server='10.xx.xx.2')
NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

with cond:
    print("Waiting")
    if not notified[0]:
        cond.wait()

# Insert your processing code here

table = NetworkTablesInstance.getTable('SmartDashboard')

# This retrieves a boolean at /SmartDashboard/foo
foo = table.getBoolean('foo', True)

print("Connected!")




