##################################################################################
# Script : 1_7.py [Problem 1.7, Pg. 73]
# Author : Akshay Peshave (peshave1@umbc.edu)
# Desc   : Reset MxN matrix rows and columns if the contain a 0 element
##################################################################################

import sys

def resetMatrix(inputMatrix):
	row_vector=range(0,len(inputMatrix))
	col_vector=range(0,len(inputMatrix[0]))
	
	row_reset_list=[]
	col_reset_list=[]
	for row in row_vector:
		col_deletion_list=[]
		for col in col_vector:
			if not inputMatrix[row][col]: 
				col_deletion_list.append(col)
				row_reset_list.append(row)
				col_reset_list.append(col)
		for col in col_deletion_list:
			del col_vector[col_vector.index(col)]
	for row in row_reset_list:
		inputMatrix[row]=[0 for i in range(0,len(inputMatrix[0]))]
	inputMatrix=list(map(list, zip(*inputMatrix)))
	for col	in col_reset_list:
		inputMatrix[col]=[0 for i in range(0,len(inputMatrix[0]))]

	return list(map(list, zip(*inputMatrix)))
inputMatrix=[[1,1,0,1],
		[1,1,1,1],
		[1,1,1,1],
		[0,1,0,1],
		[1,1,0,1],
		[0,1,1,0]]
newMatrix=resetMatrix(inputMatrix)
print("Reset Matrix:")
print(newMatrix)
