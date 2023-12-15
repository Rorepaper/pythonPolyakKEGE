from itertools import product

print("x y z w")
for x, y, z, w in product([0, 1], repeat=4):
    f = ((w or x or y) <= ((y or z) and x or y and (w or z)))
    if not f:
        print(x, y, z, w)

# x y z w
# 1 0 0 0
# 0 0 1 1
# 1 0 0 1