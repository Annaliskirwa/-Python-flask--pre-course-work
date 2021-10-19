#def get_age():
    #print("How old are you ")
    #age = int(input())
    #return age

#print(get_age())
#accepts intergers, what if a user enters a string; gets a value error; exception handling

#try/except block to handle errors
def get_age():
    print("How old are you ")
    try:
        age = int(input())
        return age
    except ValueError:
        return "That was not a valid input"