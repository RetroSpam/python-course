from abc import ABC, abstractmethod

class Fountain(ABC):
    @abstractmethod
    def spray_water(self):
        pass


class SimpleFountain:
    def spray_water(self):
        print("Simple fountain splashes water randomly")


class MusicalFountain:
    def spray_water(self):
        print("Musical fountain splashes water by rythm")


class LightedFountain:
    def spray_water(self):
        print("Lighted Fountain splashes water by lights")


fountains = [SimpleFountain(), MusicalFountain(), LightedFountain()]

for fountain in fountains:
    fountain.spray_water()