class Contact:
    """
    Class that generates new instances of contacts.
    """
    #class variable
    contact_list = [] #empty contact list
     # Init method up here
    def save_contact(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        Contact.contact_list.append(self)

    def __init__(self,first_name,last_name,phone_number,email):

      # docstring removed for simplicity

        #instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        
    def delete_contact(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Contact.contact_list.remove(self)
#new_contact.first_name