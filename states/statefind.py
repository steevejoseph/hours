#!usr/bin/env python3

"""
Simple python program that returns the  US state name that corresponds
with a user-submitted abbreviation.
"""

from US import states

def find_state(string):

	if len(string) != 2:
		print("Sorry, abbreviations must be two letters!")
		print("Please try again\n")
		main()

	try:
		retval = states[string]
		return states[string]

	except KeyError as e:
		print("No state has the abbreviation \"" + string
		+ "\"! Please try again!\n")
		main()

	#return retval

def main():
	string = input("Please enter a state's abbreviation \n")
	string = string.upper()

	print("The elongated form of " + string + "'s abbreviation is: \""
		  + find_state(string) + "\".")


if __name__ == '__main__':
	main()