from ipaddress import *

c = 0
network = ip_network("165.44.96.0/255.255.248.0", 0)
for ad in list(network):
    if "111" in bin(int(ad))[2:]:
        c += 1
print(c)
