from random import randint

#Variables
userInput = ""
flipCount = []
threeHeads = "HHH"
threeTails = "TTT"

# User Input
userInput = int(input("How many simulations do you want to run?: "))
print ()

# Input validation
if not userInput:
	quit("Nothing Inputted")
elif userInput <= 0:
	quit("Input was less than 1")

# Process
for coin in range(0, userInput):
	coins = ""
	count = 0

	while threeHeads not in coins and threeTails not in coins:
		randomCoin = randint(1, 2)

		if randomCoin == 1:
			coins += 'H'
		else:
			coins += 'T'

		count += 1

	print ("Sim " + str(coin + 1) + ": " + coins + " Flips: " + str(count))	
	flipCount.append(count)

minCount = min(flipCount)
maxCount = max(flipCount)
averageCount = sum(flipCount) / len(flipCount)

# Output
print ("\nMinimum Number of Flips: " + str(minCount))
print ("Maximum Number of Flips: " + str(maxCount))
print ("Average Number of Flips: " + str(averageCount))
