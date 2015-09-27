##################################################################################
# Script : 1_5.py [Problem 1.5, Pg. 73]
# Author : Akshay Peshave (peshave1@umbc.edu)
# Desc   : English alphabet string compression
##################################################################################

import sys

def compressString(inputString):
	compressedString=[]
	previousCharacter=''
	characterCount=0
	for character in inputString:
		if(previousCharacter <> character):
			if previousCharacter<>'': compressedString.append(previousCharacter+str(characterCount))
			previousCharacter = character
			characterCount = 1
		else:
			characterCount += 1
	
	if previousCharacter<>'': compressedString.append(previousCharacter+str(characterCount))
	
	return ''.join(compressedString)

compressedString = compressString(sys.argv[1])
print("Compressed String: ",compressedString)
