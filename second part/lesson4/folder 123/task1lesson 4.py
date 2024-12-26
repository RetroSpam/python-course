def round_to_nearest_integer():
    try:
       
        value = float(input("Enter a float value: "))
     
        rounded_value = float(round(value))
    
        print(rounded_value)
    except ValueError:
        print("Please enter a valid float number.")

round_to_nearest_integer()
