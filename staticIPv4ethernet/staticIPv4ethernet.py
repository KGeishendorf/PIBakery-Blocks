#!/usr/bin/python

#
#
#
# 2016/09/23 First version Kevin Geishendorf (kg)

#ip = sys.argv[1]
#netmask = sys.argv[2]

ip = "192.168.0.0"
netmask = "255.255.255.0"


lines = []
with open('/Users/kg2/Desktop/PIBakeryBlocks/staticIPv4ethernet/dhcpcd.conf') as infile:
	for line in infile:
		if "interface eth0" in line:
			line = line.replace("interface eth0", "interface eth0\nstatic ip_address=" + ip + "\nnetmask="+ netmask)
		lines.append(line)
with open('/Users/kg2/Desktop/PIBakeryBlocks/staticIPv4ethernet/dhcpcd.conf', 'w') as outfile:
	for line in lines:
		outfile.write(line)
