originalString = input("Enter what you want to make into an acronym: ")

words = originalString.split(" ")

acronym = ""

for x in words:
	acronym = acronym + x[:1]
	
print("Your new acronym is %s" % acronym)

input("Press 'Enter' to exit the program.")