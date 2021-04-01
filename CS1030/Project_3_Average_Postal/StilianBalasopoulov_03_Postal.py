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
isUrban = False
isRural = False

# Input / Output
while True:
	userInput = input("Enter a valid Postal Code: ").upper()

	if not userInput:
		break

	# Checking first character
	if len(userInput) != 7:
		print("Length does not equal 7")
	elif userInput[0] not in postalCodes:
		print("Not a valid location")

	# Checking second character for a 0
	if userInput[1] == '0':
		isRural = True
		isUrban = False
	else:
		isRural = False
		isRural = True

	# Determine if format of the whole string is correct

	# Output
	print("Location: " + postalCodes[userInput[0]])

	if isRural:
		print("Location is Rural")
	elif isUrban:
		print("Location is Urban")

"""	for val in userInput:
		if val % 2 == 0:
			if val.isdigit():"""








