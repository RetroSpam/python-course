class Person:
    population = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = 2024
        age = current_year - birth_year
        instance = cls(name, age)
        return instance

    @classmethod
    def print_population(cls):
        print(f"Current population: {cls.population}")

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

person1 = Person("Hassan", 29)
person1.display_info()
Person.print_population()

person2 = Person.from_birth_year("Ahab", 1993)
person2.display_info()
Person.print_population()

person3 = Person("Oksana", 37)
person3.display_info()
Person.print_population()