from ipaddress import ip_network

for mask in range(1, 33):
    n1 = ip_network(f"121.171.15.70/{mask}", False)
    n2 = ip_network(f"121.171.3.68/{mask}", False)
    if n1 == n2:
        print(n1.netmask)