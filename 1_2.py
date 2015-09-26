##################################################################################
# Script : 1_2.py [Problem 1.2, Pg. 73]
# Author : Akshay Peshave (peshave1@umbc.edu)
# Desc   : Reverse a given string
##################################################################################
import sys

def reverseString(inputString):
	temp=''
	inputStringLength = len(inputString)-1
	inputString = list(inputString)
	for index in range(0,int(inputStringLength/2)+1):
		if index==inputStringLength-index or index > inputStringLength-index:
			return ''.join(inputString)
		temp = inputString[index]
		inputString[index]=inputString[inputStringLength-index]
		inputString[inputStringLength-index]=temp
	return ''.join(inputString)

reversedString = reverseString(sys.argv[1])
print("Reversed string: ",reversedString)
