class Greenhouse:
    def __init__(self):
        self.__temperature = 0
        self.__humidity = 0
        self.__light_level = 0

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, temperature):
        if 15 <= temperature <= 30:
            self.__temperature = temperature
        else:
            raise ValueError("Temperature must be between 15 and 30 degrees.")

    def get_humidity(self):
        return self.__humidity

    def set_humidity(self, humidity):
        if 0 <= humidity <= 100:
            self.__humidity = humidity
        else:
            raise ValueError("Humidity must be between 0 and 100 percent.")

    def get_light_level(self):
        return self.__light_level

    def set_light_level(self, light_level):
        if 0 <= light_level <= 100:
            self.__light_level = light_level
        else:
            raise ValueError("Light level must be between 0 and 100.")

greenhouse = Greenhouse()

try:
    greenhouse.set_temperature(25)
    greenhouse.set_humidity(60)
    greenhouse.set_light_level(80)
except ValueError as e:
    print(e)

print("Temperature:", greenhouse.get_temperature())
print("Humidity:", greenhouse.get_humidity())
print("Light Level:", greenhouse.get_light_level())