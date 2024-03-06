from ipaddress import ip_network, ip_address

for n in range(32, 1, -1):
    ad1 = ip_network(f"140.37.235.224/{n}", False)
    ad2 = ip_network(f"140.37.235.192/{n}", False)
    if ad1.network_address == ad2.network_address:
        print(ad1.netmask, n)