from ipaddress import ip_network

for i in ip_network("192.168.248.176/255.255.255.240", False):
    s = bin(int(i))[2:]
    if s.count("1") > s.count("0"):
        print(s)
