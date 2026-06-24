contact_book = {}
while True:
    print("""Add Contact : add
Remove Contact : remove
View Contacts : view
Search Contacts : search
Change Number : num
Change Name : name""")
    print()

#User Response 
    user_response = (input("What would you like to do : "))
    print()

#Add Contacts

    if user_response == "add":
        contact_name_add = (input("Enter Name : "))

        if contact_name_add in contact_book:
            print("The Contact Already Exists")
            print()
            continue   # goes back to the main menu

        while True:
            contact_num_add = (input("Enter Number : "))

            if len(contact_num_add) == 10:
                contact_book[contact_name_add] = contact_num_add
                print(f"{contact_name_add} is added to your CONTACT BOOK")
                break
            else:
                print("The Number is Wrong")
                
                
#Remove Contacts
    elif(user_response == "remove"):
        remove_contact = input("Enter Name : ")
        
        for key in contact_book:
            if(key == remove_contact):
                contact_book.pop(remove_contact)
                print(f"{remove_contact} has been removed from your CONTACT BOOK")
                break
            else:
                print(f"The Contact {remove_contact} does not exist")
        
#View Contacts
    elif(user_response == "view"):
        contact_book_sorted = sorted(contact_book)
        if(len(contact_book_sorted)>=1):
            print("CONTACT BOOK")
            for key in contact_book_sorted:
                print(f"{contact_book_sorted.index(key) + 1}) {key} : {contact_book[key]}")
                
        else:
            print("CONTACT BOOK \nEMPTY")
            
#Search Contacts
    elif(user_response == "search"):
        print("Find with Name : name \nFind with Number : num ")
        
        print()
        user_response_search = input("Enter Response : ")
        if(user_response_search == "name"):
            contact_name_add = input("Enter name : ")
            if contact_name_add in contact_book:
                print()
                print("CONTACT DETAILS")
                print(f"{contact_name_add} : {contact_book[contact_name_add]}")
            else:
                print("Contact Name not present in CONTACT BOOK")
                
        elif(user_response_search == "num"):
            contact_num_add = input("Enter Number : ")

            old_name = None

            for key, value in contact_book.items():
                if value == contact_num_add:
                    old_name = key
                    print()
                    print("COMNTACT DETAILS")
                    print(f"{key} : {contact_num_add}")
                    break
                else:
                    print()
                    print("The Number is INVALID")
                    continue
           
           
        else:
            print()
            print("INVALID RESPONSE")
            print()
            continue

#Change Number for name
    elif(user_response == "num"):
        
        
        contact_name_add = input("Enter Name : ")
        for key in contact_book:
            
            if (key == contact_name_add):
                 
                while True:
            
                    contact_num_add = input("Enter Updated Number : ")
        
                    if(len(contact_num_add) == 10):
                        contact_book.update({contact_name_add : contact_num_add})
                        print(f"Number of {contact_name_add} has been Updated")
                        break
                    else:
                        print("The Number is Wrong")
                        print()
                        print(f"Name : {contact_name_add}")
            else:
                print("NO CONTACT FOUND")
            
#Change Name for number
    elif(user_response == "name"):
        contact_num_add = input("Enter Number : ")

        old_name = None

        for key, value in contact_book.items():
            if value == contact_num_add:
                old_name = key
                print(f"Contact Saved as : {key}")
                break

        if old_name:
            contact_name_add = input("Enter Updated Name : ")

            contact_book[contact_name_add] = contact_book[old_name]
            del contact_book[old_name]
            print(f"The contact name for the number {contact_num_add} is updated to {contact_name_add} ")
        
        else:
            print("Number not found")
    else:
        print("INVALID RESPONSE !")
    print()
    
        
    