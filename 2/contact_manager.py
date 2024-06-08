def add(contacts, name, pn, email):
    contacts.append({'Name': name, 'Phone Number': pn, "Email Address": email})

def display(contacts):
    if contacts == []:
        print("Contact list is empty!")
    for contact in contacts:
        print(f"Name: {contact['Name']}")
        print(f"Phone Number: {contact['Phone Number']}")
        print(f"Email Address: {contact['Email Address']}")
    
    
def search(contacts, name):
    for contact in contacts:
        if contact['Name'].lower() == name.lower():
            return contact
    return None

def delete(contacts, name):
    for i, contact in enumerate(contacts):
        if contact['Name'].lower() == name.lower():
            return contacts.pop(i)
        
        return None