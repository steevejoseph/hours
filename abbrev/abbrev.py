#!usr/bin/env python3

"""
Simple python program that rudimentarily abbreviates a str.
"""

def abbrev(string):
	if len(string) <= 4:
		return string
	else:
		return string[:4] + '.'


def main():
	string = input("Please enter a string \n")
	print("The abbreviated form of your string: \"" + string 
			+ "\" is "
			+ abbrev(string))

if __name__ == '__main__':
	main()