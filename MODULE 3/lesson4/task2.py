from typing import Protocol

class FileHandler(Protocol):
    def read(self) -> str:
        ...
        
    def write(self, data: str) -> None:
        ...

class TextFileHandler:
    def read(self) -> str:
        print("Reading from a text file.")
        return "Text data"
        
    def write(self, data: str) -> None:
        print(f"Writing '{data}' to a text file.")

class BinaryFileHandler:
    def read(self) -> str:
        print("Reading from a binary file.")
        return "Binary data"
        
    def write(self, data: str) -> None:
        print(f"Writing '{data}' to a binary file.")

def save_data(handler: FileHandler, data: str) -> None:
    handler.write(data)

if __name__ == "__main__":
    text_handler = TextFileHandler()
    binary_handler = BinaryFileHandler()

    save_data(text_handler, "Hello, World!")
    save_data(binary_handler, "01010101")