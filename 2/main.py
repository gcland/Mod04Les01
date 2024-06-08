import contact_manager
contacts = []
while True:
    print("\n1. Add a Contact\n2. Display All Contacts\n3. Search Contacts\n4. Delete Contact\n5. Quit")
    func = input("Choose an option:\n >> ")
    if func == "1":
        name = input("Enter contact Name: ")
        pn = input("Enter contact Phone Number: ")
        email = input("Enter contact Email Address: ")
        contact_manager.add(contacts, name, pn, email)
    elif func == "2":
        contact_manager.display(contacts)
            
    elif func == "3":
        name = input("Enter contact name to search for: ")
        c = contact_manager.search(contacts, name)
        if c:
            print(f"{name} found!")
        else:
            print(f"({name} not found.")
    elif func == "4":
        name = input("Enter contact name to delete: ")
        if contact_manager.delete(contacts, name) is not None:
            print(f"{name} deleted.")
        else:
            print(f"{name} not found.")
    elif func == "5":
        break
    else:
        print("Invalid selection. Please try again.")