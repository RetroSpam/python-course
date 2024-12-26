def convert_and_multiply() -> None:
    user_input: str = input("Enter string: ")
    try:
        number: int = int(user_input)
        result: int = number * 2
        print(str(result))
    except ValueError:
        print("Error: Enter a numeric value.")

convert_and_multiply()
