# class for the individual contacts
class Contact:
    def __init__(self, name, phone_number, email='', address=''):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class Contactbook:
    def __init__(self, contacts:dict[Contact] = {}):
        #Structure is a dictionary with the name of the contact as the key and a list of the contact object as value
        self.contacts = contacts

    def add_contact(self, contact: Contact):
        try:
            for contact_name in self.contacts:                                                               # Seaching the contact name
                for _contact in self.contacts[contact_name]:                                                 # Searching the respective/found contact name to attain the phone number
                    if _contact.phone_number == contact.phone_number:
                        return print("A contact with this phone number already exists")
            self.contacts[contact.name] = [*self.contacts[contact.name], contact]                            # Creating a list with old contact plus the new contact
        except Exception as e :
            self.contacts[contact.name] = [contact] # {"B Wilson": [Contact(name, address...)],}

    def remove_contact(self, name):
        try:
            del self.contacts[name]
        except Exception as e:
         print("Contact does not exist")


    def search_contact_by_name(self,name):
        try:
            contact_list = self.contacts[name]
            self.display_contacts({name: contact_list})
        except Exception as e:
            print("Contact does not extist")

    def search_contact_by_phone_number(self, phone_number):
        for key in self.contacts:
            contact_list = self.contacts[key]
            for contact in contact_list:                                                            #checking if the phone number exists
                if contact.phone_number == phone_number:
                    return self.display_contacts({contact.name: [contact]})
        return print("Could not find a contact with that phone number")


    def display_contactbook(self):
        self.display_contacts(self.contacts)
    
    #Helper Function to display individual contact in a nice format
    def display_contacts(self, contacts: dict):
        num = 1
        print("=========================================================================================================================")
        print("|No.| Name            | Number           | Address:                            | Email:                                  ")
        print("=========================================================================================================================")
        for contact_name in contacts:
            contact_list = contacts[contact_name]
            for contact in contact_list:
                email = contact.email if contact.email != '' else "No Email"
                address = contact.address if contact.address != '' else "No Address"
                print(f"|{num} .| {contact.name:<15} | {contact.phone_number:<15}  | {address:<34}  | {email:<35} ")
                num += 1
        print("=========================================================================================================================")


# creating a new instance of the contact book
contactbook = Contactbook()

