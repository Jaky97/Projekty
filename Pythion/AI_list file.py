#made code that saves informations about people in it eaven after closing the program. It uses a file to store the data.
# This program keeps a list of people entered and remembers them using a file.
import json

# File to store the data
DATA_FILE = "people_data.json"

# Function to load data from the file
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist
    except json.JSONDecodeError:
        return []  # Return an empty list if the file is corrupted

# Function to save data to the file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Function to add a person to the list
def add_person(name, age):
    people = load_data()
    people.append({"name": name, "age": age})
    save_data(people)
    print(f"Added {name}, age {age}.")

# Function to display all people
def display_people():
    people = load_data()
    if not people:
        print("No people in the list.")
    else:
        print("People in the list:")
        for person in people:
            print(f"- {person['name']}, age {person['age']}")

# Main program loop
def main():
    while True:
        print("\nMenu:")
        print("1. Add a person")
        print("2. Display all people")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = input("Enter age: ")
            add_person(name, age)
        elif choice == "2":
            display_people()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()