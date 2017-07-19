import bluetooth
import time

sock=bluetooth.BluetoothSocket(bluetooth.L2CAP)

#bd_addr ="C8:F7:33:12:2B:53" # Hollis laptop
bd_addr ="28:18:78:48:90:7C" # Hollis surface
#bd_addr ="B8:27:EB:05:DD:D3" #pi


port = 0x1001

sock.connect((bd_addr, port))
while 1:
    msg = raw_input('Message to send : ')
    a = time.time
    sock.send(msg)
    b = time.time
    print "Sent in "+str(b-a)+" seconds."
    if msg == '-1':
        break
sock.close()
