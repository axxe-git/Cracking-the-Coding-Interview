##################################################################################
# Script : 1_1.py [Problem 1.1, Pg. 73]
# Author : Akshay Peshave (peshave1@umbc.edu)
# Desc   : Determine if a given string has all unique characters
#
# Assumptions: strings are made up of english alphabet and comparison is case
#	       insensitive
##################################################################################
import string

def checkCharacterUniqueness(inputString):
	#initialize alphabet map
	characterMap = dict.fromkeys(string.ascii_lowercase,False)
	
	if len(inputString) > len(characterMap): return False

	inputString = inputString.lower()	
	for character in inputString:
		if characterMap[character]:
			return False
		characterMap[character]=True
	return True
	

inputString = input("Enter string: ")
flag = checkCharacterUniqueness(inputString)
print("Characters are unique." if flag else "Characters are not unique.")
