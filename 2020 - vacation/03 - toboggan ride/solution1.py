from mapping import Map


trees = 0
m = Map.from_file()

m.walk(3, 1)
while m.is_inside():
    if m.tree_here():
        trees += 1
    m.walk(3, 1)

print("number of trees =", trees)
