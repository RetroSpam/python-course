def create_workspace_layout(size):
    layout = [[0 for _ in range(size)] for _ in range(size)]
    
    for i in range(size):
        layout[i][i] = 0
    
    for i in range(size):
        layout[i][size - 1 - i] = 5
        
    if size % 2 == 1:
        center = size // 2
        layout[center][center] = 0
    
    comfort_level = 1
    for layer in range((size + 1) // 2):
        for i in range(layer, size - layer):
            if layout[layer][i] == 0:
                layout[layer][i] = comfort_level
                comfort_level += 1
        
        for i in range(layer + 1, size - layer):
            if layout[i][size - 1 - layer] == 0:
                layout[i][size - 1 - layer] = comfort_level
                comfort_level += 1
        
        for i in range(size - 2 - layer, layer - 1, -1):
            if layout[size - 1 - layer][i] == 0:
                layout[size - 1 - layer][i] = comfort_level
                comfort_level += 1
        
        for i in range(size - 2 - layer, layer, -1):
            if layout[i][layer] == 0:
                layout[i][layer] = comfort_level
                comfort_level += 1
    
    return layout

def print_layout(layout):
    for row in layout:
        print(" ".join(map(str, row)))

size = int(input("Enter the size of the work area: "))
layout = create_workspace_layout(size)
print("Workplace layout:")
print_layout(layout)