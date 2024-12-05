import csv

FILENAME = "contacts.csv"

def load_contacts():
    #Load contacts from the CSV file.
    try:
        with open(FILENAME, mode="r", newline="") as file:
            FileReader = csv.DictReader(file)
            return list(FileReader)  
        
    except Exception as e:
        return []  

def save_contacts(contact):
    
    #Append a contact to the CSV file.
    file_exists = False
    
    try:
        with open(FILENAME, "r") as file:
            file_exists = True
            
    except Exception as e:
        pass

    with open(FILENAME, "a", newline="") as file:
        fieldnames = ["name", "email", "phone", "address"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader() 
        writer.writerow(contact)  
