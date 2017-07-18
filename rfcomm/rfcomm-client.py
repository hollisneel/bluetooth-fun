import bluetooth
import time 
bd_addr ="28:18:78:48:90:7C"

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

while 1:
    msg = raw_input("Message to send : ")
    if msg == '-1':
        sock.send(msg)
        break
    a = time.time()
    sock.send(msg)
    b = time.time()
    print b-a

sock.close()
