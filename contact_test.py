import unittest
from contact import Contact


class TestContact(unittest.TestCase):

    def setUp(self):
        self.new_contact = Contact(
            "markian", "mumba", "0720120193", "markat@gmail.com")

    def tearDown(self):
        Contact.Contact_list = []

    def test_contact(self):
        self.assertEqual(self.new_contact.firstname, "markian")
        self.assertEqual(self.new_contact.lastname, "mumba")
        self.assertEqual(self.new_contact.number, "0720120193")
        self.assertEqual(self.new_contact.email, "markat@gmail.com")

    def test_save_contact(self):

        self.new_contact.save_contact()
        self.assertEqual(len(Contact.Contact_list), 1)

    def test_save_multiple(self):

        self.new_contact.save_contact()
        self.another_contact = Contact(
            "bobby", "wine", "0738291107", "mariogotse@gmai.com")
        self.another_contact.save_contact()
        self.assertEqual(len(Contact.Contact_list), 2)

    def test_delete_contact(self):
        self.new_contact.save_contact()
        test_contact = Contact("Test", "user", "0712345678",
                               "test@user.com")
        test_contact.save_contact()
        self.new_contact.remove_contact()
        self.assertEqual(len(Contact.Contact_list), 1)

    def test_find_contact_by_number(self):

        self.new_contact.save_contact()
        test_contact = Contact("Test", "user", "0711223344", "test@user.com")  
        test_contact.save_contact()
        found_contact = Contact.find_by_number("0711223344")
        self.assertEqual(found_contact.email, test_contact.email)


if __name__ == '__main__':
    unittest.main()
