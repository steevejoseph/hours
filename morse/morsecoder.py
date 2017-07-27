#!usr/bin/env python3

"""
Simple python program that encodes a plaintext messafge to morse code
"""
from morse import morseAlphabet

def morser(string):
	
	string = string.upper()
	code = ""

	for letter in string:
		if letter == " ":
			code += " "
		
		else:
			try:
				code += morseAlphabet[letter]
			except KeyError as e:
				print("Error! The character: '" + letter +
						"' is not defined in the provided dictionary.")
				print("Exiting program!")
				exit()
			

	return code

def main():
	string = input("Please enter a message to be encoded.\n")
	string = string.upper()


	print("The morse code form of " + string + " is:\n\""
		  + morser(string) + "\".")


if __name__ == '__main__':
	main()