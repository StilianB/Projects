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
	'X': 'Nunavut',
	'x': 'Northwest Territories',
	'Y': 'Yukon'
}

userInputList = []

while True:
	userInput = input("Enter your postal code: ").upper()

	if not userInput:
		break

	if userInput[0] in postalCodes:
		print(postalCodes[userInput[0]])
		userInputList.append(userInput)
	else:
		print("First letter doesn't reference a province.")
print(userInputList)