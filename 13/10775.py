from ipaddress import *

net = ip_network("156.128.0.227/255.255.255.248", False)
print(bin(int(ip_address("156.128.0.227"))), bin(int(net.netmask)), sep="\n")
