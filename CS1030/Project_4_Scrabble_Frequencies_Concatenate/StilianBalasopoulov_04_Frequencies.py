# Initial Letter Count & Variables
characters = {
	'A': 0, 'B': 0, 'C': 0,
	'D': 0, 'E': 0, 'F': 0,
	'G': 0, 'H': 0, 'I': 0,
	'J': 0, 'K': 0, 'L': 0,
	'M': 0, 'N': 0, 'O': 0,
	'P': 0, 'Q': 0, 'R': 0,
	'S': 0, 'T': 0, 'U': 0,
	'V': 4, 'W': 0, 'X': 0,
	'Y': 0, 'Z': 0
}
output = open("StilianBalasopoulov_04_02_Output.txt", "w")

# Open input file and capitalize each line
with open("1030 Project 04 02 Sentences.txt") as input:
	sentences = input.read().upper()

# Add count to dictionary
for char in sentences:
	if char in characters:
		characters[char] += 1

# Formatted Output
output.write("{:^5} {:^5}".format("Letter","Frequency"))

# Output each item in dictionary
for key in characters:
	output.write("\n{:^5} {:^10}".format(key, characters[key]))

# Close output file
output.close()