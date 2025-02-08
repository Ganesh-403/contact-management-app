import os

# Utility function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Sample contacts list
contacts = [
    {'name': 'Amit Kumar', 'number': '9876543210', 'email': 'amit.kumar@example.com'},
    {'name': 'Priya Sharma', 'number': '9123456789', 'email': 'priya.sharma@example.com'},
    {'name': 'Ravi Patel', 'number': '9988776655', 'email': 'ravi.patel@example.com'}
]

# Function to display all contacts
def show_contacts():
    clear_screen()
    print("Contacts:")
    if contacts:
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']}")
    else:
        print("No contacts available.")
    print("\n")

# Function to add a new contact
def add_contact():
    contacts.append({
        'name': input("Enter contact name: ").strip(),
        'number': input("Enter contact number: ").strip(),
        'email': input("Enter contact email: ").strip()
    })
    print("Contact added successfully!\n")

# Helper function to find a contact by name
def get_contact_by_name(name):
    return next((c for c in contacts if c['name'].lower() == name.lower()), None)

# Function to delete a contact
def delete_contact():
    contact = get_contact_by_name(input("Enter the name of the contact to delete: ").strip())
    if contact:
        contacts.remove(contact)
        print("Contact deleted successfully!\n")
    else:
        print("Contact not found.\n")

# Function to update contact details
def update_contact():
    contact = get_contact_by_name(input("Enter the name of the contact to update: ").strip())
    if contact:
        print("Current details:", contact)
        contact['name'] = input("Enter new name (leave blank to keep current): ").strip() or contact['name']
        contact['number'] = input("Enter new number (leave blank to keep current): ").strip() or contact['number']
        contact['email'] = input("Enter new email (leave blank to keep current): ").strip() or contact['email']
        print("Updated contact details:", contact)
    else:
        print("Contact not found.\n")

# Function to open a contact and allow actions
def open_contact():
    contact = get_contact_by_name(input("Enter the name of the contact to open: ").strip())
    if contact:
        print("Contact details:", contact)
        action = input("Press 'u' to update or 'd' to delete this contact: ").lower()
        if action == 'u':
            update_contact()
        elif action == 'd':
            delete_contact()
        else:
            print("Invalid input. No action taken.\n")
    else:
        print("No match found.\n")

# Main application loop
def contact_app():
    while True:
        clear_screen()
        print("Contact Management App")
        print("1. Show all contacts")
        print("2. Add a new contact")
        print("3. Open a contact")
        print("4. Update a contact")
        print("5. Delete a contact")
        print("q. Quit")
        
        choice = input("Choose an option: ").lower()
        
        actions = {
            '1': show_contacts,
            '2': add_contact,
            '3': open_contact,
            '4': update_contact,
            '5': delete_contact
        }
        
        if choice == 'q':
            print("Exiting the application.")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid option, please try again.\n")
        
        input("Press Enter to continue...")

if __name__ == "__main__":
    contact_app()
