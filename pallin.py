def is_palindrome(input_string):
	input_string =input_string.replace(" ", "")
	input_string = input_string.upper()
	# We'll create two strings, to compare them

	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for i in range(len(input_string)):
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		if (input_string[i]!="" and input_string[len(input_string)-1-i] !=""):
			new_string = new_string+input_string[i]
			reverse_string = reverse_string + input_string[len(input_string)-1-i]
	# Compare the strings

	if (new_string==reverse_string):
		return True
    
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True