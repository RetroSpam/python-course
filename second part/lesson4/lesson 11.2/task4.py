def convert_units_with_while(values, unit):
    i = 0
    while i < len(values):
        if unit == 'meters':
            converted_value = values[i] * 3.28084
            print(f"{values[i]} meter(s) = {converted_value:.5f} foot(feet)")
       
        i += 1

convert_units_with_while([1, 2], 'meters')