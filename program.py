from password import Password


userInput = ''
userPassword = Password()


while userInput != "quit":
	userInput = input("Enter Password\n")

	userPassword.setPassword(userInput)

	if(userPassword.isCommonWord()): 
		print("Password is a common word")
		userPassword.calculateScore()
		userPassword.printReport()

	else:
		userPassword.calculateScore()
		userPassword.printReport()