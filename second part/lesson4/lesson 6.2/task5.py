a = input("input prices: ")
b =[int(x) for x in a.split(',')]
b.sort()
print(b)

b[0], b[-1] = b[-1], b[0]

print(f"new prices:{b}")