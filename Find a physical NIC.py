import wmi

w = wmi.WMI()

for n in w.Win32_NetworkAdapter():
    if n.MACADDress is None or n.PhysicalAdapter == False:
        continue
    mac = n.MACADDress
    name = n.Name
    print("%s: %s" % (name,mac))