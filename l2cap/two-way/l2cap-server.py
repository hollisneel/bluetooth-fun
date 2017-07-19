import bluetooth

server_sock=bluetooth.BluetoothSocket( bluetooth.L2CAP )

port = 0x1001
server_sock.bind(("",port))
server_sock.listen(1)

client_sock,address = server_sock.accept()
print "Accepted connection from ",address
print " "

while 1:
    data = client_sock.recv(1024)
    print "received [%s]" % data

    if data == '-1':
        client_sock.send('-1')
        break

    msg = raw_input("Message to send : ")
    client_sock.send(msg)

    if msg == '-1':
        break

client_sock.close()
server_sock.close()
