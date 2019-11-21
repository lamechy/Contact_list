class Contact:
    """
    Class that generates new instances of contacts.
    """
    def __init__(self,first_name,last_name,number,email):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email
    contact_list = [] # Empty contact list
    def save_contact(self):
        Contact.contact_list.append(self)

    