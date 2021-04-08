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

# Checking each character for formatting mistakes and string information
def postalAssignment(user, postal):
	digitCount = 0
	upperCount = 0
	spaceCount = 0
	firstCharacterCheck = False
	formatBool = False
	digit = [1, 4, 6]
	upper = [0, 2, 5]

	# Checking first character
	if len(user) != 7:
		print("Length does not equal 7")
	elif user[0] not in postal:
		print("Location not in dictionary")
	else:
		firstCharacterCheck = True


	# Checking second character
	if user[1] == '0':
		isRural = True
	else:
		isRural = False

	# Checking entire string formatting
	for var in range(len(user)):

		if var in upper:
			if user[var].isupper():
				upperCount += 1
		elif var in digit:
			if user[var].isdigit():
				digitCount += 1
		else:
			if user[var].isspace():
				spaceCount += 1

	if upperCount == 3 and digitCount == 3 and spaceCount == 1 and firstCharacterCheck:
		formatBool = True

	return formatBool, isRural

# Input / Output
while True:
	userInput = input("Enter a valid Postal Code: ").upper()

	if not userInput:
		break

	# Determine if format is correct and if postal code is rural
	formattingCheck, isRural = postalAssignment(userInput, postalCodes)

	# Output
	if formattingCheck:
		print("Location: " + postalCodes[userInput[0]])
	
		if isRural:
			print("Location is Rural")
		else:
			print("Location is Urban")
