def reverse_words(input_string):
    
    words = input_string.split()
    
    reversed_words = ' '.join(word[::-1] for word in words)
    return reversed_words


input_string = "Hello World"
output_string = reverse_words(input_string)
print(output_string)


input_string = "Python"
output_string = reverse_words(input_string)
print(output_string)