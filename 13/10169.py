from ipaddress import *

for mask in range(33):
    net = ip_network(f"157.127.182.76/{mask}", False)
    net2 = ip_network(f"157.127.190.80/{mask}", False)
    if net.network_address != net2.network_address:
        print(bin(int(net.netmask))[2:].count("1"))