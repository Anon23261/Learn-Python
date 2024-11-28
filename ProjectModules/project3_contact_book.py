# Project Module 3: Contact Book

# Implement a simple contact book application.
# Use data structures like lists or dictionaries to store contact information.

# Example Code:

contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact {name} added.")

def view_contacts():
    for name, phone in contacts.items():
        print(f"Name: {name}, Phone: {phone}")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print("Contact not found.")

# Example usage
add_contact("Alice", "123-456-7890")
view_contacts()
delete_contact("Alice")
