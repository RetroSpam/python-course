import csv

def main():
    with open('clients.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Surname", "Birthday", "Bonuses"])
        
        print("Good day! Enter your data:")
        
        while True:
            name = input("Name: ")
            if name.lower() == "stop":
                break
            surname = input("Last name: ")
            birthday = input("Date of birth (DD.MM.YYYY): ")
            bonuses = input("Bonus balance: ")
            
            writer.writerow([name, surname, birthday, bonuses])
            
            print(f"Thank you! Client {name} was added!")

if __name__ == "__main__":
    main()