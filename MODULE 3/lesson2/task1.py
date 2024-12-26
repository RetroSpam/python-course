class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = 2024
        age = current_year - birth_year
        return cls(name, age)

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

person1 = Person("Hassan", 29)
person1.display_info()

person2 = Person.from_birth_year("Ahab", 1993)
person2.display_info()

person3 = Person.from_birth_year("Natsha", 1990)
person3.display_info()
