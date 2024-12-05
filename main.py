#Contact Book Management System

#from contact_operations import add_contact, view_contacts, remove_contact, search_contact
#from file_manager import load_contacts, save_contacts

# Load contacts at the start
# contacts = load_contacts()


while True:
    print("\n=== Contact Book Management System ===")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Remove Contact")
    print("4. Search Contact")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
        
    if choice == '1':
        # add_contact(contacts)
        # save_contacts(contacts)
        print(f"Added")     
    elif choice == '2':
        # view_contacts(contacts)            
        print("View")
    elif choice == '3':
        # remove_contact(contacts)
        # save_contacts(contacts)
        print("Remove")

    elif choice == '4':
        # search_contact(contacts)
        print("Search")

    elif choice == '5':
        print("Thanks for using Contact Book Management System. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please try again.")
     
