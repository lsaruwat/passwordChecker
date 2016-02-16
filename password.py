passwords = []

with open("passwords.txt", "r") as inputFile:
	for line in inputFile:
		passwords.append(line)

print(len(passwords))