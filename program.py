from password import Password


userInput = ''

while userInput != "quit":
	userInput = input("Enter Password\n")

	userPassword = Password(userInput)

	userPassword.getDictionary()

	if(userPassword.isCommonWord()): 
		print("Password is a common word")
		userPassword.calculateScore()
		userPassword.printReport()

	else:
		userPassword.calculateScore()
		userPassword.printReport()