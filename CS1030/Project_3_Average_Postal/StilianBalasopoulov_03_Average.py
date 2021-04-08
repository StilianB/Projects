print("Enter as many numbers at wanted, type '0' to quit.")

# Variables
usrList = []
avgList = []
higher = []
lower = []

# Checking if user input is valid
def inputValidation(usrList):
	while True:
		usrInput = input("> ")

		if not usrInput or usrInput == '0':
			break
		else:
			try:
				usrInput = int(usrInput)
				usrList.append(usrInput)
			except ValueError:
				print("Input was not an int")

# Find the average given user input
def findAvg(usr):
	try:
		average = int(sum(usr) / len(usr))
	except ZeroDivisionError:
		average = 0

	return average

# Sort existing user inputted list
def sortList(usr, avg, higher, lower):
	for var in usr:
		if var == average:
			avg.append(var)
		elif var < average:
			lower.append(var)
		else:
			higher.append(var)

# Process functions
inputValidation(usrList)
average = findAvg(usrList)
sortList(usrList, avgList, higher, lower)

# Output
print("\nUser inputted list: " + str(usrList))
print("Average: " + str(average))
print("\nHigher: " + str(higher))
print("Lower: " + str(lower))
print("Average: " + str(avgList))