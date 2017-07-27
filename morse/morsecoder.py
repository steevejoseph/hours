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
			code += morseAlphabet[letter]

	return code

def main():
	string = input("Please enter a message to be encoded.\n")
	string = string.upper()


	print("The morse code form of " + string + " is:\n\""
		  + morser(string) + "\".")


if __name__ == '__main__':
	main()