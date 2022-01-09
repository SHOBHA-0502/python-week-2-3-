def format_name(first_name, last_name):
	if first_name !="" and last_name !="":
		return last_name ,first_name
	elif first_name != ""and last_name =="":
		return first_name
	elif first_name == "" and last_name !="":
		return last_name

	


a,b = format_name("Ernest", "Hemingway")
print(a,b)
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string