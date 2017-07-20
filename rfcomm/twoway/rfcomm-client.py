import bluetooth
import time 

def utf8len(s):
    return len(s.encode('utf-8'))

#bd_addr ="C8:F7:33:12:2B:53" # Hollis laptop
#bd_addr ="28:18:78:48:90:7C" #Surface
bd_addr ="B8:27:EB:05:DD:D3" #pi

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
    print "---- Sending Stats ----"
    print "Send Time : " ,round(b-a,6)
    print "Bluetooth Speed [%s] B/s" %round(utf8len(msg)/(b-a),2)
    print " "
    print "Waiting on incoming message ..."
    data = sock.recv(65536) # recieve 1024 bytes
    print "Received [%s]" %data
    print " "
sock.close()
