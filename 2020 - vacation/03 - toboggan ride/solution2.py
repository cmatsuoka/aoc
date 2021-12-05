from mapping import Map

    
params = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

total = 1
for args in params:
    trees = 0
    m = Map.from_file()

    m.walk(*args)
    while m.is_inside():
        if m.tree_here():
            trees += 1
        m.walk(*args)

    print(f"number of trees for {args} = {trees}")
    total *= trees

print("total =", total)
