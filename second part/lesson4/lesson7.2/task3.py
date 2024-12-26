def print_selected_numbers(numbers):
    n = numbers[0]
    m = numbers[-1]
    k = numbers[1]

    selected_numbers = []
    for i in range(n, m + 1, k):
        if i in numbers:
            selected_numbers.append(i)


    print(", ".join(map(str, selected_numbers)))

print_selected_numbers([1, 2, 3, 4, 5])
print_selected_numbers([2, 1, 6])
