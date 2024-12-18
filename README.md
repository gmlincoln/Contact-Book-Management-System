# Contact Book Management System

A Command Line Interface (CLI) project built in Python for managing a contact book. This application uses a CSV file for storing and managing contacts persistently.

---

## **Features**
- Add contacts with fields: **Name**, **Email**, **Phone Number**, and **Address**.
- Prevent duplicate phone numbers.
- View all saved contacts in a user-friendly format.
- Search for contacts by phone number.
- Remove contacts by phone number.
- Save contact data to a CSV file automatically.
- Load contacts from the CSV file when the program starts.

---

## **File Structure**

project-directory/

├── main.py  # Main Python script containing the application logic

├── contact_operations.py  # Main Python script containing the application logic

├── file_manager.csv # CSV file storing all contacts(auto-generated on first run)

├──  README.md  # Project documentation (this file)


## **CSV File Details**

The contacts.csv file is created automatically when the program is run for the first time.

It contains the following fields:
- **name** 
- **email** 
- **phone** 
- **address** 

## **Menu Options**
- **Add Contact:** Input details to create a new contact.
- **View Contacts:** Display all contacts in a formatted list.
- **Search Contact:** Search for a contact using their phone number.
- **Remove Contact:** Delete a contact by phone number.
- **Exit:** Close the application.



---

### How to Use
- Clone this repository and run the `main.py` file from your terminal.

