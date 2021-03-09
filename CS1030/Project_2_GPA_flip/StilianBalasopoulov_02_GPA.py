# Documentation
print("Enter the grades below, when finished leave the last space empty. Your GPA will then be calculated.")

# Variables
sumOfPoints = 0
numOfGrades = 0
gpa = 0.0
userInput = ""
grades = []
gradeDict = {'A+': 4.2, 
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

while userInput != "QUIT" or not userInput:
	userInput = input("Grade: ").upper()

	if userInput in gradeDict:
		grades.append(userInput)
		numOfGrades += 1
	else:
		print("Please enter a valid grade.")

if not grades:
	quit("No grades were inputted.")

for grade in grades:
	if grade in gradeDict:
		sumOfPoints += gradeDict[grade]

gpa = sumOfPoints / numOfGrades

# Output
print("Final GPA: " + str(round(gpa, 1)))