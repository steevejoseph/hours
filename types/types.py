#!usr/bin/env python3

"""
Simple python program that encodes a plaintext messafge to morse code
"""

from ast import literal_eval


def tiptype(string):
	try:
		int(string)
		return ["Oranges! ", "<class 'int'>"]

	except ValueError as e:
		if type(string) == str:
			return ["Apples! ", type(string)]

	else:
		return ["Bananas! ", type(string)]


def get_type(string):
	try:
		return type(literal_eval(string))
	except (ValueError, SyntaxError):
		return str

def main():
	
	word = input("Please enter something: \n")


	listy = tiptype(word)
	print(listy[0] + "Your thing is of type: " + str(listy[1]))

	print("Your thing, \"" + word 
			+ "\" is of type: " + str(get_type(word)))


if __name__ == '__main__':
	main()