#!/usr/bin/env python3.6

#the shebang 

from contact import Contact
def create_contact(fname,lname,phone,email):
    '''
    Function to create a new contact
    '''
    new_contact = Contact(fname,lname,phone,email)
    return new_contact

def save_contacts(contact):
    '''
    Function to save contact
    '''
    contact.save_contact()

def del_contact(contact):
    '''
    Function to delete a contact
    '''
    contact.delete_contact()