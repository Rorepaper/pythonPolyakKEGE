from ipaddress import *

for mask in range(33):
    net1 = ip_network(f"151.172.115.121/{mask}", False)
    net2 = ip_network(f"151.172.115.156/{mask}", False)
    if net1.network_address != net2.network_address:
        print(mask)
        break
