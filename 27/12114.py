from itertools import product
print('x y z w f')
for x, y, z, w in product([0,1], repeat=4):
    f = (x <= y) and ((not y) == z) and w
    if f == 1:
        print(x, y, z, w, f)