import sys

# User Input & Validation
keepGoing = True
while keepGoing:
	feet = input("Enter your Height in feet: ")

	if not feet:
		sys.exit("Nothing inputted")

	inches = input("Enter the remaining inches: ")

	if not inches:
		sys.exit("Nothing inputted")
	elif int(inches) > 12:
		sys.exit("Inches must be less than 12")

	verification = input("You're total height is " + str(feet) + "ft " + str(inches) + "in? (y/n): ")

	if verification == "y":
		keepGoing = False
	else:
		print("Please re-enter the details below.")

# Computation
feet = int(feet)
inches = int(inches)
totalInches = inches + (feet * 12)
centimeters = totalInches * 2.54
meters = centimeters // 100
centimetersRemaining = (round(centimeters / 100, 2) - meters) * 100

# Output
if totalInches >= 96:
	print("Wow! You're really tall.")

print(str(feet) + "ft " + str(inches) + "in is " + str(int(meters)) + "m " + str(int(centimetersRemaining)) + "cm")