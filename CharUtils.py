class CharUtils(object):
	#make dictionary of symbols for sequential comparison. Ugly but straightforward
	numberSymbol = {')':0,'!':1,'@':2,'#':3,'$':4,'%':5,'^':6,'&':7,'*':8,'(':9,')':10} # web app symbol set

	def __init(self):
		print("------------Built this thing--------------") #I don't plan on instantiating this class so if I see this then something is wrong

		
	@staticmethod
	def isSymbol(char):
		if not char.isalpha() and not char.isdigit() and char != ' ':
			return True
		else:
			return False

	@staticmethod
	def isSymbol2(char): # this is how the web app interperets symbols
		numberSymbolStr = ")!@#$%^&*()"
		return True if char in numberSymbolStr else False