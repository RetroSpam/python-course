def consolidate_files():
    first_file = input("Enter the name of the first file: ")
    last_file = input("Enter the name of the last file: ")

    first_number = int(first_file.split('.')[0])
    last_number = int(last_file.split('.')[0])

    with open('for_buh.txt', 'w') as output_file:
        for file_number in range(first_number, last_number + 1):
            file_name = f"{file_number}.txt"
            try:
                with open(file_name, 'r') as input_file:
                    content = input_file.read()
                    output_file.write(content + "\n")
            except FileNotFoundError:
                print(f"Warning: {file_name} not found. Skipping this file.")

    print("All files have been successfully consolidated into for_buh.txt.")

consolidate_files()