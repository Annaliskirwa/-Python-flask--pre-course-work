import unittest # Importing the unittest module
from contact import Contact # Importing the contact class

class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

# Items up here .......

    def setUp(self): #define instructions that will be executed before each test method
        '''
        Set up method to run before each test cases.
        '''
        self.new_contact = Contact("James","Muriuki","0712345678","james@ms.com") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        #checks for an expected result
        self.assertEqual(self.new_contact.first_name,"James")
        self.assertEqual(self.new_contact.last_name,"Muriuki")
        self.assertEqual(self.new_contact.phone_number,"0712345678")
        self.assertEqual(self.new_contact.email,"james@ms.com")


    #this test case shoul pass after adding the save contact method in tge cintact file
    def test_save_contact(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_contact.save_contact() # saving the new contact
        self.assertEqual(len(Contact.contact_list),1)

if __name__ == '__main__':
    unittest.main() #command line interface that collects all the tests methods and executes them.

