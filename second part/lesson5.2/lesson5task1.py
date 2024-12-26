def swap_parts(name):
 
    mid = len(name) // 2
   
    return name[mid:] + name[:mid]


names = ["Logomachine", "ArtSpace", "Designify"]
swapped_names = [swap_parts(name) for name in names]

for original, swapped in zip(names, swapped_names):
    print(f'Original: {original}, Swapped: {swapped}')
