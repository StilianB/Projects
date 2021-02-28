# User Input & Validation
feet = input("Enter your Height in feet: ")
inches = input("Enter the remaining inches: ")

if not feet or not inches:
	quit("Nothing inputted")
elif int(inches) > 12:
	quit("Inches must be less than 12")

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

print(str(feet) + "ft " + str(inches) + "in is " 
	+ str(int(meters)) + "m " + str(int(centimetersRemaining)) + "cm")