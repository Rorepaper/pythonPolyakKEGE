from itertools import product
print("a b c t")
for a, b, c, t in product([0, 1], repeat=4):
    f = ((not a) or (not b)) and (c <= (not a)) and (t and (not a) or c and (not b))
    print(a, b, c, t, 0 if f else 1)