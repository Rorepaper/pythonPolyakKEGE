from itertools import product
print("x y w z")
for x, y, w, z in product([0, 1], repeat=4):
    f = (not ((not (x <= (not w))) or z)) or (not(w <= z)) or (x <= (not z))

    print(x, y, w, z, f)
