pointTable = {
	'A': 1,
	'B': 3,
	'C': 3,
	'D': 2,
	'E': 1,
	'F': 4,
	'G': 2,
	'H': 4,
	'I': 1,
	'J': 8,
	'K': 5,
	'L': 1,
	'M': 3,
	'N': 1,
	'O': 1,
	'P': 3,
	'Q': 10,
	'R': 1,
	'S': 1,
	'T': 1,
	'U': 1,
	'V': 4,
	'W': 4,
	'X': 8,
	'Y': 4,
	'Z': 10
}
scores = []

# Calculating score of each word
def findScore(words, points, scores):
	for line in words:
		line = line.upper()
		score = 0

		if not line:
			continue

		for char in line:
			if char in points and char.isalpha():
				score += points[char]
		scores.append(score)
	
	return scores

# Accessing Text Document with Words
with open("1030 Project 04 01 Words.txt") as input:
	words = input.read().splitlines()

# Remove blank list values
for word in words:
	if not word:
		words.remove(word)

# Setting list of scores
scores = findScore(words, pointTable, scores)

# Formatted output to file
output = open("StilianBalasopoulov_04_01_Output.txt", "w")
output.write("{:^15}|{:^15}".format("Words","Points"))
output.write("\n-------------------------------\n")

for i in range(len(words) - 1):
	output.write("{:<15}|{:>15}\n".format(str(words[i]), str(scores[i])))

output.write("-------------------------------\n")
output.write("{:^15}|{:^15}".format("Total:",str(sum(scores))))


