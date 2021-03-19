print("Enter as many numbers at wanted, type '0' to quit.")

# Variables
usrList = []
avgList = []
higher = []
lower = []
average = 0

# User Input
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

# Find Average
try:
	average = int(sum(usrList) / len(usrList))
except ZeroDivisionError:
	pass

# Sort into lists
for var in usrList:
	if var == average:
		avgList.append(var)
	elif var < avg:
		lower.append(var)
	else:
		higher.append(var)

# Output
print("\nUser inputted list: " + str(usrList))
print("Average: " + str(avg))
print("\nHigher: " + str(higher))
print("Lower: " + str(lower))
print("Average: " + str(avgList))