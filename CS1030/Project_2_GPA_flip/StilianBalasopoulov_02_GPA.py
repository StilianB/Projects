# Documentation
print("Enter the grades below, when finished leave the last space empty. Your GPA will then be calculated.")

# Variables
gpa = 0.0
gpaList = []
overallGpa = 0
gradeCount = 0
studentCount = 1
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

# Loop for each student
while True:
	print("Student " + str(studentCount))
	count = 0
	gpa = 0.0
	
	# User Input / Grade Input
	while True:
		userInput = input("Grade: ").upper()

		# Input validation
		if not userInput or userInput == 'QUIT':
			break

		# GPA dictionary conversion
		if userInput in grades:
			gpa += grades[userInput]
			count += 1
		elif not userInput or userInput == 'QUIT':
			print("Calculating GPA...")
		else:
			print("Please enter a valid grade")

	# GPA Calculation
	if count > 0:
		gpa	/= count
	else:
		break

	# Individual student output
	gpaList.append(gpa)
	print("Student " + str(studentCount) + " GPA : " + str(gpa) + "\n")
	studentCount += 1

# Overall gpa calc
for gpa in gpaList:
	overallGpa += gpa
overallGpa /= studentCount - 1

# Overall output
print("Overall GPA: " + str(overallGpa))