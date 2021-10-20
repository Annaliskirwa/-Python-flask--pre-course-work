# function which return reverse of a string

def isPalindrome(s):
	return s == s[::-1]


# Driver code
s ="11211"
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")



# Recursive function to check if a
# string is palindrome

def isPalindrome(s):
	
	#to change it the string is similar case
	s = s.lower()
	# length of s
	l = len(s)
	
	# if length is less than 2
	if l < 2:
		return True

	# If s[0] and s[l-1] are equal
	elif s[0] == s[l - 1]:
		
		# Call is pallindrome form substring(1,l-1)
		return isPalindrome(s[1: l - 1])

	else:
		return False

# Driver Code
s = "MalaYaLam"
ans = isPalindrome(s)

if ans:
	print("Yes")

else:
	print("No")