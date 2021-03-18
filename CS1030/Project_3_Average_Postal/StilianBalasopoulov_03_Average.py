"""Below and Above Average – List Practice

Write a program that reads integers from a user and 
places them into a list. Stop entering numbers when 
he user enters a 0. Don’t put the 0 in the list. 
Display the average of all the numbers in the list. 
Then using three lists one after the other, display 
all numbers that are below the average, that equal 
the average, and that are above the average. 
Include an appropriate title at the start of each 
of the three lists. Allow for the possibility that 
there are no numbers below the average and no numbers 
above the average. (What does that mean about the 
numbers in the list?)"""

"""
User Input
	if user enters 0 stop entering numbers
	dont put 0 into the list
put user input into list
display the average of all numbers in list
	avg = sum(list) / len(list)
create 3 lists
	1 for all numbers lower than average
	1 for all numbers equal to average
	1 for all numbers higher than average

	for i in range(len(userInput))
		check if number is ><= avg
		put in corresponding list

Formatted output showing userInput list,
avg, and the remaining lists

"""