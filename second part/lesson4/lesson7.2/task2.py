def sum_of_elements(input_list):
    if len(input_list) < 4:
        return sum(input_list[1:])  
    return sum(input_list[1:4]) 


input1 = [1, 2, 3, 4, 5]
input2 = [10, 20, 30]

output1 = sum_of_elements(input1)
output2 = sum_of_elements(input2)

print("Output 1:", output1) 
print("Output 2:", output2)
