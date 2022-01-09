def format_name(first_name, last_name):
	if first_name !=""and last_name !="":
		return last_name ,first_name
	elif first_name != ""and last_name =="":
		return first_name
	elif first_name == "" and last_name !="":
		return last_name

	


print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string

def fractional_part(numerator, denominator):
	if(denominator==0):
		return 0
	elif(numerator ==0 or numerator==denominator):
		return 0
	
	else:
		return (numerator/denominator)%1
	

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0