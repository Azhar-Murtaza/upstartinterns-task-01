import json
import os

FILE_NAME = "contacts.json"


# Load contacts from JSON file
def load_contacts():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


# Save contacts to JSON file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


# Add a contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)

    print("Contact added successfully!")


# List all contacts
def list_contacts(contacts):
    if len(contacts) == 0:
        print("No contacts found.")
        return

    print("\n--- Contact List ---")

    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")
        print()


# Search contacts
def search_contacts(contacts):
    search = input("Enter name to search: ").lower()

    found = False

    for contact in contacts:
        if search in contact["name"].lower():
            print("\nName:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            found = True

    if not found:
        print("No matching contact found.")


# Edit a contact
def edit_contact(contacts):
    list_contacts(contacts)

    if len(contacts) == 0:
        return

    try:
        number = int(input("Enter contact number to edit: "))

        if number < 1 or number > len(contacts):
            print("Invalid contact number.")
            return

        contact = contacts[number - 1]

        name = input(f"Enter new name ({contact['name']}): ")
        phone = input(f"Enter new phone ({contact['phone']}): ")
        email = input(f"Enter new email ({contact['email']}): ")

        if name != "":
            contact["name"] = name

        if phone != "":
            contact["phone"] = phone

        if email != "":
            contact["email"] = email

        save_contacts(contacts)

        print("Contact updated successfully!")

    except ValueError:
        print("Please enter a valid number.")


# Delete a contact
def delete_contact(contacts):
    list_contacts(contacts)

    if len(contacts) == 0:
        return

    try:
        number = int(input("Enter contact number to delete: "))

        if number < 1 or number > len(contacts):
            print("Invalid contact number.")
            return

        deleted = contacts.pop(number - 1)

        save_contacts(contacts)

        print(f"{deleted['name']} deleted successfully!")

    except ValueError:
        print("Please enter a valid number.")


# Main program
def main():
    contacts = load_contacts()

    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add contact")
        print("2. List contacts")
        print("3. Search contact")
        print("4. Edit contact")
        print("5. Delete contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            list_contacts(contacts)

        elif choice == "3":
            search_contacts(contacts)

        elif choice == "4":
            edit_contact(contacts)

        elif choice == "5":
            delete_contact(contacts)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()