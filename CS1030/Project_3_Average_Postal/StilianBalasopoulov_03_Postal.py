"""
Odd characters are letters
Even characters are numbers

check the first value (userInput[0]) is in postalCodes
	if not then output invalid input

check the second value if its 0 or otherwise
0 is rural
anything else is urban

Input
validate the input - if invalid then print why
if user hits enter end the program
"""
# Variables
postalCodes = {
	'A': 'Newfoundland',
	'B': 'Nova Scotia',
	'C': 'Prince Edward Island',
	'E': 'New Brunswick',
	'G': 'Quebec',
	'H': 'Quebec',
	'J': 'Quebec',
	'K': 'Ontario',
	'L': 'Ontario',
	'M': 'Ontario',
	'N': 'Ontario',
	'P': 'Ontario',
	'R': 'Manitoba',
	'S': 'Saskatchewan',
	'T': 'Albera',
	'V': 'British Columbia',
	'X': 'Nunavut or Northwest Territories',
	'Y': 'Yukon'
}

formattingCheck = False
isRural = False

def postalAssignment(user, postal):
	digitBool = False
	upperBool = False
	formatBool = False
	digit = [1, 4, 6]
	upper = [0, 2, 5]

	# Checking first character
	if len(user) != 7:
		print("Length does not equal 7")
	elif user[0] not in postal:
		print("Location not in dictionary")

	# Checking second character
	if user[1] == '0':
		isRural = True
	else:
		isRural = False

	# Checking entire string formatting
	for var in range(len(user)):
		if var in digit:
			if user[var].isdigit():
				digitBool = True
		elif var in upper:
			if user[var].isupper():
				upperBool = True

	if digitBool and upperBool:
		formatBool = True

	return formatBool, isRural

# Input / Output
while True:
	userInput = input("Enter a valid Postal Code: ").upper()

	if not userInput:
		break

	formattingCheck, isRural = postalAssignment(userInput, postalCodes)

	# Output
	if formattingCheck:
		print("Location: " + postalCodes[userInput[0]])
	
		if isRural:
			print("Location is Rural")
		else:
			print("Location is Urban")
