import bluetooth

sock=bluetooth.BluetoothSocket(bluetooth.L2CAP)

#bd_addr ="C8:F7:33:12:2B:53" # Hollis laptop
bd_addr ="28:18:78:48:90:7C" # Hollis surface

port = 0x1001

sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()
