#!usr/bin/env python3

"""
Function that returns the infinitive form of a gerund
"""

def gerund_infinitive(string):
	string = string.lower()


	if (string[-3:] != "ing") or (len(string) <=4):
		print(string + " is not a gerund!")
		return ""

	else:
		return "to " + string[0:-3]

def main():
	word = input("Please enter a gerund:\n")

	if gerund_infinitive(word):
		print("The infinitive of " + word + " is: " + 
		gerund_infinitive(word))	

if __name__ == '__main__':
	main()
