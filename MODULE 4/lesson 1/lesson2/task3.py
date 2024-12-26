import csv
import json
from datetime import datetime, date

class Client:
    def __init__(self, name, surname, birthday, bonuses):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.bonuses = bonuses

    def is_valid_name(self):
        return all('А' <= char <= 'я' or char == ' ' for char in self.name)

    def is_valid_surname(self):
        return all('А' <= char <= 'я' or char == ' ' for char in self.surname)

    def is_valid_birthday(self):
        try:
            birth_date = datetime.strptime(self.birthday, "%m/%d/%Y").date()
            return date(1950, 1, 1) <= birth_date <= date.today()
        except ValueError:
            return False

    def is_valid_bonuses(self):
        try:
            bonuses = int(self.bonuses)
            return 0 <= bonuses <= 10000000
        except ValueError:
            return False

    def is_valid(self):
        return (self.is_valid_name() and
                self.is_valid_surname() and
                self.is_valid_birthday() and
                self.is_valid_bonuses())

def process_clients(file_path):
    processed_clients = []
    skipped_count = 0

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            client = Client(row['Name'], row['Surname'], row['Birthday'], row['Bonuses'])
            if client.is_valid():
                processed_clients.append({
                    "name": client.name,
                    "surname": client.surname,
                    "birthday": client.birthday,
                    "Bonuses": int(client.bonuses)
                })
            else:
                skipped_count += 1

    with open('clients.json', 'w', encoding='utf-8') as jsonfile:
        json.dump({"clients": processed_clients}, jsonfile, ensure_ascii=False, indent=4)

    print(f"Processed(clients): {len(processed_clients)}")
    print(f"Missed(clients): {skipped_count}")
process_clients('clients.csv')