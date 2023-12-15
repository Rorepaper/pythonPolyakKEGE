from ipaddress import *

for i in range(256):
    net = ip_network(f"187.124.21.237/{16+bin(i)[2:].count('1')}", False)
    address = bin(int(net.network_address))[2:]

    fl = False
    if address[:16].count("1") < address[16:].count("1"):
        fl = True

    if not fl:
        print(i)