# Define the Contact class
class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

# Define the ContactBook class
class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print(f"Added contact: {name}")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term in contact.name or search_term in contact.phone]
        if not found_contacts:
            print("No contacts found.")
        else:
            for contact in found_contacts:
                print(contact)

    def update_contact(self, search_term):
        for contact in self.contacts:
            if search_term in contact.name or search_term in contact.phone:
                print("Current contact details:")
                print(contact)
                contact.name = input("Enter new name: ")
                contact.phone = input("Enter new phone number: ")
                contact.email = input("Enter new email: ")
                contact.address = input("Enter new address: ")
                print("Contact updated.")
                return
        print("Contact not found.")

    def delete_contact(self, search_term):
        for contact in self.contacts:
            if search_term in contact.name or search_term in contact.phone:
                self.contacts.remove(contact)
                print("Contact deleted.")
                return
        print("Contact not found.")

# Display the menu options
def display_menu():
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

# Main function to run the application
def main():
    contact_book = ContactBook()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)

        elif choice == '4':
            search_term = input("Enter name or phone number to update: ")
            contact_book.update_contact(search_term)

        elif choice == '5':
            search_term = input("Enter name or phone number to delete: ")
            contact_book.delete_contact(search_term)

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    main()
