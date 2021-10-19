#Indexes in dictionaries are called keys, can be integers / strings
#The values are called values

# Creating empty dictionaries
my_dict = {}
my_dict = dict()

# Creating a dictionary with keys and values
my_cat = {'name':'Mr sniffles','age':18, 'color':'black'}
cat_name = my_cat['name']


birthdays = {"John":"August 1","Marcus":"April 8"}
birthdays["mary"] = "September 14"
print(birthdays) # this prints {"John":"August 1","Marcus":"April 8","Mary":"September 14"}
print(birthdays.keys()) # this prints dict_keys(['John', 'Marcus', 'Mary'])
print(birthdays.values())
print(list(birthdays.keys()))
print(cat_name) # 'Mr sniffles'
