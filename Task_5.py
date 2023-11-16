contacts = {}

def add_contact(name, phone_number, email, address):
    contacts[name] = {"Phone": phone_number, "Email": email, "Address": address}
    print(f"Contact '{name}' added.",format(name))

def list_contacts():
    if contacts:
        print("Contact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['Phone']}")
    else:
        print("No contacts found.")

def search_contact(query):
    results = [(name, details) for name, details in contacts.items() if query.lower() in name.lower()]
    if results:
        print("Search Results:")
        for name, details in results:
            print(f"Name: {name}, Phone: {details['Phone']}",format(name))
    else:
        print("No matching contacts found.")

def update_contact(name, new_phone_number, new_email, new_address):
    if name in contacts:
        contacts[name]["Phone"] = new_phone_number
        contacts[name]["Email"] = new_email
        contacts[name]["Address"] = new_address
        print(f"Contact '{name}' updated.",format(name))
    else:
        print(f"Contact '{name}' not found.",format(name))

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.",format(name))
    else:
        print(f"Contact '{name}' not found.",format(name))

if __name__ == "_main_":
    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(name, phone_number, email, address)
        elif choice == "2":
            list_contacts()
        elif choice == "3":
            query = input("Enter name to search: ")
            search_contact(query)
        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            update_contact(name, new_phone_number, new_email, new_address)
        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            delete_contact(name)
        elif choice == "6":
            break
