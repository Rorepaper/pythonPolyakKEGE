from ipaddress import *

for mask in range(33):
    net = ip_network(f"201.92.0.20/{mask}", False)
    net2 = ip_network(f"201.92.0.49/{mask}", False)
    if net.network_address == net2.network_address:
        print(mask)
        print(net.network_address)