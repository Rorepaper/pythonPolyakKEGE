from ipaddress import *

for mask in range(33):
    network = ip_network(f"111.91.200.28/{mask}", False)
    if network.network_address == ip_address("111.91.192.0"):
        print(bin(int(network.netmask))[2:])