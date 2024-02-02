print(max([len(i) - 3 if i[:2] == "XY" and i[-1] == "Z" else len(i) for i in
           open("6837pol.txt").readline().split("XYZ")]))
