from CharUtils import CharUtils# static methods to help with the madness

class Password(object):

	def __init__(self, _userPassword):
		self.userPassword = _userPassword
		self.length = len(_userPassword)
		self.score = 0


	def getDictionary(self):
		self.dictionary = [] 
		self.weakDictionary = []

		with open("passwords.txt", "r") as inputFile:
			for line in inputFile:
				line = line.strip() # strip endl char

				if len(line) < 8: self.weakDictionary.append(line) # these are words that aren't long enough 
				else: self.dictionary.append(line)

		print("weak: {}".format(len(self.weakDictionary)))
		print("strong: {}".format(len(self.dictionary)))

	def getWeakDictionary(self):
		self.weakDictionary = []

		for password in self.dictionary:
			if len(password) < 8: self.weakDictionary.append(self.weakDictionary)

	def isCommonWord(self): # Brute force method. This is order of n at worse but it's 1 line :)
		return True if self.userPassword in self.dictionary else False

	def isLongEnough(self):#
		return True if self.length >= 8 else False

	def countUppercase(self):
		uppercase = 0

		for char in self.userPassword:
			if char.isupper(): uppercase += 1
		return uppercase

	def countLowercase(self):
		lowercase = 0

		for char in self.userPassword:
			if char.islower(): lowercase += 1
		return lowercase

	def countNumbers(self, _str):
		numbers = 0

		for char in _str:
			if char.isdigit():
				numbers += 1
		return numbers

	def countSymbols(self, _str):
		symbols = 0
		for char in _str:
			if CharUtils.isSymbol(char): # if it isn't a number, alpha, or space, it should be something weird(symbol)
				symbols += 1
		return symbols
	
	def countMiddleSpecials(self): #count symbols and numbers that are in the middle. This is apparently unexpected and more secure
		middleSpecials = 0

		numbers = self.countNumbers(self.userPassword[1 : len(self.userPassword)-1]) # colon notation to grab only the middle of string
		symbols = self.countSymbols(self.userPassword[1 : len(self.userPassword)-1])

		middleSpecials += numbers # add the number count for middle str
		middleSpecials += symbols # add the symbol count for middle str

		return middleSpecials

	def countRequirements(self): # this is another weird one. requirements points only kick in after 4 or more are met. requirements are boolean in nature
		requirements = 0

		#this is gross but straightforward... I think
		if self.lowercase: requirements +=1
		if self.uppercase: requirements +=1
		if self.numbers: requirements +=1
		if self.symbols: requirements +=1
		if self.middleSpecials: requirements +=1

		return requirements

	def onlyLetters(self):
		deduction = 0

		#if self.symbols + self.numbers == 0: # This is how I think the web version is doing this... counting spaces as letters
		if self.length == self.uppercase + self.lowercase: # The web version counts spaces as letters which I consider to be broken. This will not count spaces as letters
			deduction = self.length
		return deduction

	def onlyNumbers(self):
		deduction = 0

		if self.length == self.numbers: # 
			deduction = self.length
		return deduction

	def repeatChars(self):
		#todo make this function
		return 0

	def consecutiveUppercase(self):
		deduction = 0

		for i in range(len(self.userPassword)-1): # -1 on the range to avoid stepping outside of list
			if self.userPassword[i].isupper() and self.userPassword[i+1].isupper():
				deduction += 1
		return deduction

	def consecutiveLowercase(self):
		deduction = 0

		for i in range(len(self.userPassword)-1): # -1 on the range to avoid stepping outside of list
			if self.userPassword[i].islower() and self.userPassword[i+1].islower():
				deduction += 1
		return deduction

	def consecutiveNumber(self):
		deduction = 0

		for i in range(self.length-1): # -1 on the range to avoid stepping outside of list
			if self.userPassword[i].isdigit() and self.userPassword[i+1].isdigit():
				deduction += 1
		return deduction

	def sequencedLetters(self, _str):
		deduction = 0
		_str = _str.upper()
		for i in range(len(_str)-2):
			if _str[i].isalpha() and ord(_str[i]) == ord(_str[i+1])-1 and ord(_str[i+1]) == ord(_str[i+2])-1: #ord converts char to int
				deduction += 1
		return deduction

	def sequencedNumbers(self, _str):
		deduction = 0

		for i in range(len(_str)-2):
			if _str[i].isdigit() and _str[i+1].isdigit() and _str[i+2].isdigit(): #all three are digits so wwe can cast without errors
				if int(_str[i]) == int(_str[i+1])-1 and int(_str[i+1]) == int(_str[i+2])-1: #convert chars to ints if they are digits
					deduction += 1
		return deduction
	
	def sequencedSymbols(self, _str): #What is a sequential symbol? Ascending ascii? Ascending unicode? No, Only keyboard layout matters
		deduction = 0

		for i in range(len(_str)-2):
			if CharUtils.isSymbol2(_str[i]) and CharUtils.isSymbol2(_str[i+1]) and CharUtils.isSymbol2(_str[i+2]): #all three are symbols
				if CharUtils.numberSymbol[_str[i]] == CharUtils.numberSymbol[_str[i+1]]-1 and CharUtils.numberSymbol[_str[i+1]] == CharUtils.numberSymbol[_str[i+2]]-1: # this is madness. checks dictionary of symbols mapped to ints
					deduction += 1
		return deduction

	def getProperties(self):
		self.lowercase = self.countLowercase()
		self.uppercase = self.countUppercase()
		self.numbers = self.countNumbers(self.userPassword)
		self.symbols = self.countSymbols(self.userPassword)
		self.middleSpecials = self.countMiddleSpecials()
		self.requirements = self.countRequirements()

		self.lettersOnly = self.onlyLetters()
		self.numbersOnly = self.onlyNumbers()
		self.repeats = self.repeatChars()
		self.consecutiveUpper = self.consecutiveUppercase()
		self.consecutiveLower = self.consecutiveLowercase()
		self.consecutiveNum = self.consecutiveNumber()
		self.sequentialLetters = self.sequencedLetters(self.userPassword)
		self.sequentialNumbers = self.sequencedNumbers(self.userPassword)
		self.sequentialSymbols = self.sequencedSymbols(self.userPassword)


	def printReport(self):
		print("Length: {}".format(self.length))
		print("Uppercase: {}".format(self.uppercase))
		print("Lowercase: {}".format(self.lowercase))
		print("Numbers: {}".format(self.numbers))
		print("Symbols: {}".format(self.symbols))
		print("Middle Specials: {}".format(self.middleSpecials))
		print("Requirements: {}".format(self.requirements))

		print("Only Letters: {}".format(self.lettersOnly))
		print("Only Numbers: {}".format(self.numbersOnly))
		print("Repeat Chars: {}".format(self.repeats))
		print("Consecutive Uppercase: {}".format(self.consecutiveUpper))
		print("Consecutive Lowercase: {}".format(self.consecutiveLower))
		print("Consecutive Numbers: {}".format(self.consecutiveNum))
		print("Sequential Letters: {}".format(self.sequentialLetters))
		print("Sequential Numbers: {}".format(self.sequentialNumbers))
		print("Sequential Symbols: {}".format(self.sequentialSymbols))


		print("SCORE: {}".format(self.score))

	def calculateScore(self):
		#Score based off of web calculator found at http://www.passwordmeter.com

		self.score = 0
		
		self.getProperties()

		#Additions
		self.score += self.length*4 # length score
		self.score += (self.length - self.uppercase)*2 # uppercase score
		self.score += (self.length - self.lowercase)*2 # lowercase score
		self.score += self.numbers*4 # numbers score
		self.score += self.symbols*6 # symbols score
		self.score += self.middleSpecials*2 # middle numbers/symbols score
		self.score += self.middleSpecials*2 # middle numbers/symbols score
		if self.requirements >= 4: # this bonus only counts if 4 or more requirements are met
			self.score += self.requirements*2

		#Deductions
		self.score -= self.lettersOnly
		self.score -= self.numbersOnly
		self.score -= self.repeats
		self.score -= self.consecutiveUpper*2
		self.score -= self.consecutiveLower*2
		self.score -= self.consecutiveNum*2
		self.score -= self.sequentialLetters*3
		self.score -= self.sequentialNumbers*3
		self.score -= self.sequentialSymbols*3