inputFile = open("1030 Project 04 03 Files.txt", 'r')
output = open("StilianBalasopoulov_04_03_Output.txt", 'w')

for file in inputFile:
	if file[-1] == '\n':
		subFile = open(file[:-1] + '.txt', 'r')
	else:
		subFile = open(file + '.txt', 'r')

	for line in subFile:
		if line[-1] == '\n':
			output.write(line)
		else:
			output.write(line + '\n')

inputFile.close()
output.close()