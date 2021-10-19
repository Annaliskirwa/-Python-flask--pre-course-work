class Contact:
    """
    Class that generates new instances of contacts.
    """
    #class variable
    contact_list = [] #empty contact list
    def __init__(self,first_name,last_name,phone_number,email):

      # docstring removed for simplicity

        #instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email