t = [1, 5, 7, 33, 39, 52]
for p in t:
    print(p)


for p in enumerate(t):
    (x, y) = p
    print(f'(x, y)= ({x}, {y})')
print(t)
print(enumerate(t))