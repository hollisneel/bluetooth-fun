import bluetooth
import time

sock=bluetooth.BluetoothSocket(bluetooth.L2CAP)

#bd_addr ="C8:F7:33:12:2B:53" # Hollis laptop
bd_addr ="28:18:78:48:90:7C" # Hollis surface
#bd_addr ="B8:27:EB:05:DD:D3" #pi

print "Welcome to l2cap fun! Please follow instructions.\n"

port = 0x1001

sock.connect((bd_addr, port))
print "Connected to ",(bd_addr, port)

print "Waiting for message..."
while 1:

    print "\n"
    msg = raw_input('Message to send : ')
    sock.send(msg)
    print "\nMessage sent.. Waiting for response...\n"

    data = sock.recv(1024)
    print "received : [%s]" %data

    if msg == '-1' or data == '-1':
        break

sock.close()
