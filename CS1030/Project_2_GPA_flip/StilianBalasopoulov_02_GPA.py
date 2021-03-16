# Documentation
print("Enter the grades below, when finished leave the last space empty. Your GPA will then be calculated.")

# Variables
keepGoing = True
gpa = 0.0
count = 0
grades = {	 'A+': 4.2, 
			 'A': 4.0, 
			 'A-': 3.9,
			 'B+': 3.7,
			 'B': 3.2, 
			 'B-': 3.0,
			 'C+':2.8,
			 'C': 2.2,
			 'C-': 2.0,
			 'D+': 1.8,
			 'D': 1.2,
			 'F': 0
		 }

# User Input
while keepGoing:
	userInput = input("Grade: ").upper()

	# Break loop if userInput is 'QUIT' or empty
	if not userInput or userInput == "QUIT":
		keepGoing = False

	# Input validation
	if userInput in grades:
		gpa += grades[userInput]
		count += 1
	elif not userInput or userInput == "QUIT":
		print("Calculating GPA...")
	else:
		print("Please enter a valid grade.")

# Calculating GPA
gpa /= count

# Output
print("Final GPA: " + str(round(gpa, 1)))