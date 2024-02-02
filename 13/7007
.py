from ipaddress import ip_network
c = 0
net = list(ip_network("117.32.0.0/255.224.0.0", False))[1:-1]
for i in net:
    if len(set(str(i).split("."))) == 3:
        c += 1
print(c)
