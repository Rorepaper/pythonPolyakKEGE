from ipaddress import ip_network
cc = 0
net = list(ip_network("216.130.64.0/255.255.192.0", False))[1:]
for i in net:
    c = 0
    for j in str(i).split("."):
        if int(j) % 2 == 0:
            c += 1
    if c == 4:
        cc += 1
print(cc)