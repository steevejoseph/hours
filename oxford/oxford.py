#!usr/bin/env python3

"""
Simple python program that adds takes in a list of 3+
items and returns it as a comma-separated list.
"""


def commafy(listy):

	if len(listy) < 3:
		print("Sorry, list must be at least three items long!\n")
		main()

	listy[-1] = "and " + listy[-1]
	return ", ".join(listy)

def main():
	indy = True
	listy = []

	while(indy == True):
		print("Welcome! How many things will you enter in the list?")
		numTings = int(input())

		if numTings < 3:
			print("Sorry, list must be at least three items long!\n")
			main()


		for i in range(numTings):
			listy.append(input("Please enter item #" + str((i+1)) + "\n") )


		print("The oxford comma formatted version of your list is: " 
				+ commafy(listy))

		comment = input("Would you like to go again? (Y/N)\n")
		print("you chose: " + comment)


		if (comment.lower() == "n") or (comment.lower() == "no"):
			indy = False
			print("Goodbye!")
			


if __name__ == '__main__':
	main()	