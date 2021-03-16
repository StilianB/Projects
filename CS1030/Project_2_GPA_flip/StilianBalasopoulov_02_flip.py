from random import randint

#Variables
userInput = ""
flipCount = []
heads = "HHH"
tails = "TTT"

# User Input
userInput = input("How many simulations do you want to run?: ")
print ()

# Input validation
if not userInput:
	quit("Nothing Inputted")
elif int(userInput) <= 0:
	quit("Input was less than 0")
else:
	userInput = int(userInput)

# Process
for coin in range(userInput):
	coins = ""
	count = 0

	while True:
		randomCoin = randint(1, 2)

		if randomCoin == 1:
			coins += 'H'
		else:
			coins += 'T'

		count += 1

		if heads in coins or tails in coins:
			break

	print ("Sim " + str(coin + 1) + ": " + coins + " Flips: " + str(count))	
	flipCount.append(count)

minCount = min(flipCount)
maxCount = max(flipCount)
averageCount = sum(flipCount) / len(flipCount)

# Output
print ("\nMinimum Number of Flips: " + str(minCount))
print ("Maximum Number of Flips: " + str(maxCount))
print ("Average Number of Flips: " + str(averageCount))