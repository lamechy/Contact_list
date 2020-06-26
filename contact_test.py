import unittest 
import pyperclip 
from contact import Contact 
class TestContact(unittest.TestCase):
   
   def setUp(self):
       self.new_contact = Contact("Nyakundi","Lamech","0790406870","Ongondi88@gmail.com")# Create contact object

   def tearDown(self):
       Contact.contact_list = []

   def test_init(self):
       self.assertEqual(self.new_contact.first_name,"Nyakundi")
       self.assertEqual(self.new_contact.last_name,"Lamech")
       self.assertEqual(self.new_contact.phone_number,"0790406870")
       self.assertEqual(self.new_contact.email,"Ongondi88@gmail.com")

   def setUp(self):
       self.new_contact = Contact("Nyakundi","Lamech","0790406870","Ongondi88@gmail.com")

   def test_save_contact(self):
        self.new_contact.save_contact()# saving the contact 
        self.assertEqual(len(Contact.contact_list),1)
   def setUp(self):
       self.new_contact = Contact("Nyakundi","Lamech","0790406870","Ongondi88@gmail.com")
  
   
   def test_save_multiple_contact(self):

       self.new_contact.save_contact()
       test_contact = Contact("Test","user","0790406870","test@user.com")
       test_contact.save_contact()
       self.assertEqual(len(Contact.contact_list),2)

   def setUp(self):
       self.new_contact = Contact("Nyakundi","Lamech","0790406870","Ongondi88@gmail.com")

   def test_delete_contact(self):
       self.new_contact.save_contact()
       test_contact = Contact("Test","user","0790406870","test@user.com")
       test_contact.save_contact()

       self.new_contact.delete_contact()
       self.assertEqual(len(Contact.contact_list),1)

   def setUp(self):
       self.new_contact = Contact("Nyakundi","Lamech","0790406870","Ongondi88@gmail.com")
   def test_find_contact_by_number(self):
       self.new_contact.save_contact()
       test_contact = Contact("Test","user","0791406870","test@user.com")
       test_contact.save_contact()

       found_contact = Contact.find_by_number("0791406870")

       self.assertEqual(found_contact.email,test_contact.email)

   def setUp(self):
       self.new_contact = Contact("Nyakundi","Lamech","0790406870","Ongondi88@gmail.com")
   def test_contact_exists(self):
       self.new_contact.save_contact()
       test_contact =  Contact("Test","user","0791406870","Ongondi88@gmail.com")
       test_contact.save_contact()

       contact_exists = Contact.contact_exist("0791406870")
       self.assertTrue(contact_exists)

   def setUp(self):
       self.new_contact = Contact("Nyakundi","Lamech","0790406870","Ongondi88@gmail.com")
   def test_diplay_all_contacts(self):
       self.assertEqual(Contact.display_contacts(),Contact.contact_list)

   def setUp(self):
       self.new_contact = Contact("Nyakundi","Lamech","0790406870","Ongondi88@gmail.com")

   def test_copy_email(self):
       self.new_contact.save_contact()
       Contact.copy_email("0790406870")

       self.assertEqual(self.new_contact.email,pyperclip.paste())

if __name__ == '__main__':
    unittest.main()
 