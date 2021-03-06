#Enter a string and the program will reverse it and print it out.

# Python3 program to print reverse
# of words in a string.

def wordReverse(str):
	i = len(str)-1
	start = end = i+1
	result = ''

	while i>=0:
		if str[i] == ' ':
			start = i+1
			while start!= end:
				result += str[start]
				start+=1
			result+=' '
			end = i
		i-=1
	start = 0
	while start!=end:
		result+=str[start]
		start+=1
	return result

# Driver Code
str = 'I am Annalis'
print(wordReverse(str))


#reversing a string using for loop
def reverse_string(str):  
    str1 = ""   # Declaring empty string to store the reversed string  
    for i in str:  
        str1 = i + str1  
    return str1    # It will return the reverse string to the caller function  
     
str = "JavaTpoint"    # Given String       
print("The original string is: ",str)  
print("The reverse string is",reverse_string(str)) # Function call  



# Reverse string  
# Using a while loop  
  
str = "JavaTpoint" #  string variable  
print ("The original string  is : ",str)   
reverse_String = ""  # Empty String  
count = len(str) # Find length of a string and save in count variable  
while count > 0:   
    reverse_String += str[ count - 1 ] # save the value of str[count-1] in reverseString  
    count = count - 1 # decrement index  
print ("The reversed string using a while loop is : ",reverse_String)# reversed string  



#  Reverse a string    
# using  slice syntax   
# reverse(str) Function to reverse a string   
def reverse(str):   
    str = str[::-1]   
    return str   
    
s = "JavaTpoint"  
print ("The original string  is : ",s)   
print ("The reversed string using extended slice operator  is : ",reverse(s))  


#reverse a string using reversed()   
# Function to reverse a string   
def reverse(str):   
    string = "".join(reversed(str)) # reversed() function inside the join() function  
    return string   
  
s = "JavaTpoint"  
  
print ("The original string is : ",s)   
print ("The reversed string using reversed() is : ",reverse(s) )  

#reversing a string using recursion
def reverse(str):   
    if len(str) == 0: # Checking the lenght of string  
        return str   
    else:   
        return reverse(str[1:]) + str[0]   