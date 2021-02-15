import sys
# User Input
magnitude = float(input("Enter a magnitude: "))


# Output
if magnitude < 0:
	sys.exit("Magnitude cannot be lower than 0.")
elif magnitude >= 0 and magnitude < 2.0:
	print("An earthquake of magnitude " + str(magnitude) + " is considered 'Micro'")
elif magnitude >= 2.0 and magnitude < 3.0:
	print("An earthquake of magnitude " + str(magnitude) + " is considered 'Very Minor'")
elif magnitude >= 3.0 and magnitude < 4.0:
	print("An earthquake of magnitude " + str(magnitude) + " is considered 'Minor'")
elif magnitude >= 4.0 and magnitude < 5.0:
	print("An earthquake of magnitude " + str(magnitude) + " is considered 'Light'")
elif magnitude >= 5.0 and magnitude < 6.0:
	print("An earthquake of magnitude " + str(magnitude) + " is considered 'Moderate'")
elif magnitude >= 6.0 and magnitude < 7.0:
	print("An earthquake of magnitude " + str(magnitude) + " is considered 'Strong'")
elif magnitude >= 7.0 and magnitude < 8.0:
	print("An earthquake of magnitude " + str(magnitude) + " is considered 'Major'")
elif magnitude >= 8.0 and magnitude < 10.0:
	print("An earthquake of magnitude " + str(magnitude) + " is considered 'Great'")
elif magnitude >= 10.0:
	print("An earthquake of magnitude " + str(magnitude) + " is considered 'Meteoric'")