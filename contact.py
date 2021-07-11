class Contact:

    Contact_list = []

    def __init__(self, firstname, lastname, number, email):
        self.firstname = firstname
        self.lastname = lastname
        self.number = number
        self.email = email

    def save_contact(self):

        Contact.Contact_list.append(self)

    def remove_contact(self):

        Contact.Contact_list.remove(self)

    @classmethod
    def find_by_number(cls, number):

        for contact in cls.Contact_list:
            if contact.number == number:
                return contact
