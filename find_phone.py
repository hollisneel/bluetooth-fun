import bluetooth



target_name     = raw_input("Device name : ")
target_address  = None

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    name =  bluetooth.lookup_name( bdaddr )
    print name
    if target_name == name:
        target_address = bdaddr
        break

if target_address is not None:
    print "Found "+ str(target_name) +" with bt address", target_address
else:
    print "Not found"
