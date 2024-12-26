from abc import ABC, abstractmethod

class Instrument(ABC):
    @abstractmethod
    def play(self) -> None:
        pass

class Guitar(Instrument):
    def play(self) -> None:
        print("Strumming the guitar strings!")

class Piano(Instrument):
    def play(self) -> None:
        print("Playing the piano keys!")

class Flute(Instrument):
    def play(self) -> None:
        print("Blowing into the flute!")

if __name__ == "__main__":
    instruments = [Guitar(), Piano(), Flute()]

    for instrument in instruments:
        instrument.play()