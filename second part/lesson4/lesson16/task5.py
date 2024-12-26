def generate_spiral_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_direction = 0
    
    row, col = 0, 0
    for num in range(1, n*n + 1):
        matrix[row][col] = num
        next_row = row + directions[current_direction][0]
        next_col = col + directions[current_direction][1]
        
        if (0 <= next_row < n and 0 <= next_col < n and matrix[next_row][next_col] == 0):
            row, col = next_row, next_col
        else:
            current_direction = (current_direction + 1) % 4
            row = row + directions[current_direction][0]
            col = col + directions[current_direction][1]
    
    return matrix

def print_spiral_matrix(matrix):
    print("Project Matrix:")
    for row in matrix:
        print(" ".join(map(str, row)))

n = int(input("Enter the width of the matrix: "))
spiral_matrix = generate_spiral_matrix(n)
print_spiral_matrix(spiral_matrix)