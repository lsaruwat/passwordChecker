
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

	def isCommonWord(self): # Brute force method. This is order of n at worse but it's 2 lines :)
		if self.userPassword in self.dictionary: return True
		else: return False

	def isLongEnough(self):#
		status = True if self.length >= 8 else False
		return status

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
			if not char.isalpha() and not char.isdigit() and char != ' ': # if it isn't a number, alpha, or space, it should be something weird(symbol)
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

	def getProperties(self):
		self.lowercase = self.countLowercase()
		self.uppercase = self.countUppercase()
		self.numbers = self.countNumbers(self.userPassword)
		self.symbols = self.countSymbols(self.userPassword)
		self.middleSpecials = self.countMiddleSpecials()
		self.requirements = self.countRequirements()


	def printReport(self):
		print("Length: {}".format(self.length))
		print("Uppercase: {}".format(self.uppercase))
		print("Lowercase: {}".format(self.lowercase))
		print("Numbers: {}".format(self.numbers))
		print("Symbols: {}".format(self.symbols))
		print("Middle Specials: {}".format(self.middleSpecials))
		print("Requirements: {}".format(self.requirements))


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
