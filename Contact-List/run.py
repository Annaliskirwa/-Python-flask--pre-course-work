#!/usr/bin/env python3.6

#the shebang 

from contact import Contact
def create_contact(fname,lname,phone,email):
    '''
    Function to create a new contact
    '''
    new_contact = Contact(fname,lname,phone,email)
    return new_contact