from itertools import product
print("x y w z")

for x, y, w, z in product([0, 1], repeat=4):
    f = ((x == z) or (not (x == w))) and ((y <= x) or (not z))
    if not f:
        print(x, y, z, w)
