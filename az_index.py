#!/usr/bin/env python3

"""
Simple python program that returns/prints "aardvark"
if the word entered begins with 'a', or "zebra" for all other letters.
"""

word = input("Please enter a word!\n")

word = word.lower()

if word[0] == 'a':
	print("aardvark!")
else:
	print("zebra!")

print(word[::-1])

	
