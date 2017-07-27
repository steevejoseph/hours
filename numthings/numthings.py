#!usr/bin/env python3
"""
Simple program that tells how many objects are ina  list,
gramatically correct. NOTE: because English has a million'
plural rule exceptions, I've chosen to only focus on a small number of
valid cases. Sorry :/
"""

def numthings(listy):
	kw1 = " is "
	kw2 = "a "
	vowels = ('a', 'e', 'i', 'o', 'u')

	listy[1] = listy[1].lower()

	if listy[0] > 1:
		kw1 = ' are '
		kw2 = str(listy[0]) + ' '

		if(listy[1][-1] == "y"):
			listy[1] = listy[1][:-3]
			listy[1] += 'ies'

		else:
			listy[1] += 's'


	elif listy[0] == 1:
		if listy[1].startswith(vowels):
			kw2 = "an "

	return "There" + kw1 +  kw2 + listy[1] + '.'





def main():
	print(numthings([1, "ice"]))


if __name__ == '__main__':
	main()