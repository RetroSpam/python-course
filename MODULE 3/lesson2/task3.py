class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Convert Celsius to Fahrenheit."""
        fahrenheit = celsius * (9/5) + 32
        return fahrenheit

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        """Convert Fahrenheit to Celsius."""
        celsius = (fahrenheit - 32) * (5/9)
        return celsius


celsius_temp = 25
fahrenheit_temp = Temperature.celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is {fahrenheit_temp}°F")

celsius_temp = 100
fahrenheit_temp = Temperature.celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is {fahrenheit_temp}°F")


fahrenheit_temp = 77
celsius_temp = Temperature.fahrenheit_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp}°F is {celsius_temp}°C")


fahrenheit_temp = 300
celsius_temp = Temperature.fahrenheit_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp}°F is {celsius_temp}°C")