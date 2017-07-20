import bluetooth
import time

def utf8len(string):
    return len(string.encode('utf-8'))

server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port = 1
server_sock.bind(("",bluetooth.PORT_ANY))
server_sock.listen(1)

client_sock,address = server_sock.accept()
print "Accepted connection from ",address
print "\nWaiting on incoming message ..."
while 1:
    print " "
    data = client_sock.recv(4294967296)
    print "Received [%s]" %data
    print " "
    if data == "-1":
        break
    
    msg = raw_input("Message to send : ")
    if msg == '-1':
        client_sock.send(msg)
        break

    a = time.time()
    client_sock.send(msg)
    b = time.time()
    print "---- Sending Stats ----"
    print "Send Time : ", round(b-a,6)
    print "Bluetooth Speed [%s] B/s" %round(utf8len(msg)/(b-a),2)
    print " "
    print "Waiting on incoming message ..."
client_sock.close()
server_sock.close()
