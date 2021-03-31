print("Enter as many numbers at wanted, type '0' to quit.")

# Variables
usrList = []
avgList = []
higher = []
lower = []

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

def findAvg(usr):
	try:
		average = int(sum(usr) / len(usr))
	except ZeroDivisionError:
		average = 0

	return average

def sortList(usr, avg, higher, lower):
	for var in usr:
		if var == average:
			avg.append(var)
		elif var < average:
			lower.append(var)
		else:
			higher.append(var)

# Operations
inputValidation(usrList)
average = findAvg(usrList)
sortList(usrList, avgList, higher, lower)

# Output
print("\nUser inputted list: " + str(usrList))
print("Average: " + str(average))
print("\nHigher: " + str(higher))
print("Lower: " + str(lower))
print("Average: " + str(avgList))