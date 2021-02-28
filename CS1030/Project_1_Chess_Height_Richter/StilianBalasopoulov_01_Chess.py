# Program Summary
print("This program takes the input of a square on a chess board(a4, b5, h8) and determines if the square is white or black.")
print("Square notation consists of a single letter(a-h) and a single digit(1-8).")

# Verify user conformed to input requirements
def userInputVerification(userInput):
	if len(userInput) != 2:
		print("Please follow input guidelines.")
	elif letter < 97 or letter > 104:
		print("The letter has to be between a and h")
	elif number < 1 or number > 8:
		print("The number has to be between 1 and 8")
	else:
		return False
	return True

# Determining color of square
def getColor(pos, letter, number):
	letter -= 96
	color = "white"
	if (letter + number) % 2 == 0:
		color = "black"

	print(str(pos[0]) + str(pos[1]) + " is a " + color + " square.")

# User Input
userInput = ''
while userInputVerification(userInput) == True:
	userInput = str(input("\nPlease choose a square: "))
	letter = ord(userInput[0].lower())
	number = int(userInput[1])

# Output of square color
getColor(userInput, letter, number)