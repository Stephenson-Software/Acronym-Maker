def makeAcronym(originalString):
	words = originalString.split()

	acronym = ""

	for x in words:
		acronym = acronym + x[:1]

	return acronym


if __name__ == "__main__":
	try:
		originalString = input("Enter what you want to make into an acronym: ")
	except EOFError:
		raise SystemExit

	print("Your new acronym is %s" % makeAcronym(originalString))

	try:
		input("Press 'Enter' to exit the program.")
	except EOFError:
		pass
