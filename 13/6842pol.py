from ipaddress import ip_network
c = 0
for i in ip_network("158.132.161.128/255.255.255.128", False):
    if bin(int(i))[2:][-1] == "1":
        c += 1
print(c)
