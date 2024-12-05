from file_manager import save_contacts

def add_contact(contacts):
    
    print("\n=== Add Contact ===")
    
    #To remove whitespace use strip() 
    name = input("Enter Name: ").strip()
    email = input("Enter Email: ").strip()
    phone = input("Enter Phone Number: ").strip()
    address = input("Enter Address: ").strip()

    if not name.isalpha():
        print("Name must be a string!")
        return
    if not phone.isdigit():
        print("Phone number must be numeric!")
        return
    if phone in [contact['phone'] for contact in contacts]:
        print("This phone number already exists!")
        return
    
    new_contact = {"name": name, "email": email, "phone": phone, "address": address}
    contacts.append(new_contact)
    
    save_contacts(new_contact)
    print("Contact added successfully!")
    return contacts

def view_contacts(contacts):
    print("\n=== View Contacts ===")
    if not contacts:
        print("No contacts found!")
        return
    
    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}:")
        print(f"Name: {contact['name']}")
        print(f"Email: {contact['email']}")
        print(f"Phone: {contact['phone']}")
        print(f"Address: {contact['address']}")

def remove_contact(contacts):
    print("\n=== Remove Contact ===")
    phone = input("Enter the phone number of the contact to remove: ").strip()
    
    for contact in contacts:
        if contact['phone'] == phone:
            contacts.remove(contact)
            print("Contact removed successfully!")
            return
    
    print("Error: Contact not found!")

def search_contact(contacts):
    print("\n=== Search Contact by Phone Number ===")
    phone = input("Enter the phone number to search: ").strip()

    # Search for the contact with the phone number
    for contact in contacts:
        if contact['phone'] == phone:
            print("\nContact Found:")
            print(f"Name: {contact['name']}")
            print(f"Email: {contact['email']}")
            print(f"Phone: {contact['phone']}")
            print(f"Address: {contact['address']}")
            return
    
    print("No contact found with this phone number.")