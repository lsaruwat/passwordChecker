from password import Password


userInput = ''
userPassword = Password()


while userInput != ":q!":
	userInput = input("Enter Password\n")

	userPassword.setPassword(userInput)
	userPassword.calculateScore()
	#userPassword.printReport()
	userPassword.printScore()