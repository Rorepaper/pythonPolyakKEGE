f = {10002: 1, 10001: 1, 10000: 1}

for n in range(9999, 0, -1):
    if n % 2 != 0:
        f[n] = f[n+1] - 3
    else:
        f[n] = f[n + 3] + 7
print(f[50] - f[57])