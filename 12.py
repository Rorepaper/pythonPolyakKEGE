for a in range(3, 10001):
    n = '1' + '8' * a
    while '18' in n or '388' in n or '888' in n:
        n = n.replace('18', '8', 1)
        n = n.replace('388', '81', 1)
        n = n.replace('888', '3', 1)
    if n.count('1') == 3:
        print(a)