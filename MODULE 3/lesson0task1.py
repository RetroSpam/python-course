class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

    def eat(self, food):
        print(f"{self.name} eats {food}")

animal1 = Animal("Dog", "Woof")
animal1.make_sound()
animal1.eat("dog food")

animal2 = Animal("Cat", "Meow")
animal2.make_sound()
animal2.eat("cat food")

animal2 = Animal("Lion", "Roar")
animal2.make_sound()
animal2.eat("wild animals")

animal2 = Animal("human", "words")
animal2.make_sound()
animal2.eat("burger")