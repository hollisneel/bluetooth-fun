import bluetooth

target_name     = "hollis-laptop"#"DESKTOP-VIJD1CK"
target_address  = None

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    name =  bluetooth.lookup_name( bdaddr )
    print name
    if target_name[0:7] == name[0:7]:
        target_address = bdaddr
        break

if target_address is not None:
    print "Found iPhone with bt address", target_address
else:
    print "Not found"
