alpha = "I like old music"
password = "K34jndnks"
number_string = "12345"
tabbs = "       "
titles = "I Love Cups"
false_titles = "I love Cups"

print( alpha.isalpha() )
print( password.isalnum() )
print( number_string.isdecimal() )
print( tabbs.isspace() )
print( titles.istitle() )
print( false_titles.istitle())
#xstring methods are really useful when you want to do something like password validation


#typecasting
name = "James"
age = 19
weight = '79' # Kilograms

age_weight_ratio = int(weight)/age

print(float(age_weight_ratio))