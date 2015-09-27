##################################################################################
# Script : 1_6.py [Problem 1.6, Pg. 73]
# Author : Akshay Peshave (peshave1@umbc.edu)
# Desc   : Rotate a NxN matrix by 90 degrees
##################################################################################

import sys

def rotateMatrixBy90(inputMatrix):
	matrixRowCount = len(inputMatrix)
	loopConstraint = int(matrixRowCount/2)+1
	evenRows=False
	if loopConstraint%2 <> 0: loopConstraint+1

	for rowIndex in range(0,loopConstraint):
		for columnIndex in range(rowIndex,matrixRowCount-rowIndex-1):
			# rotation in place requires 4 matrix entries to be moved. 
			# Indices of the 4 entries are specified in transformIndices.
			transformIndices=[(rowIndex,columnIndex),						 
						(matrixRowCount-columnIndex-1,rowIndex),
						(matrixRowCount-rowIndex-1,matrixRowCount-columnIndex-1),
						(columnIndex, matrixRowCount-rowIndex-1)] 
			# Rotate the 4 entries whose indices are specified in transformIndices
			(row,column)=transformIndices[0]
			tempStore=inputMatrix[row][column]
			for i in range(1,4):
				(row,column)=transformIndices[i]
				tempStore_2=inputMatrix[row][column]
				inputMatrix[row][column]=tempStore 
				tempStore=tempStore_2
			(row,column)=transformIndices[0]
                        inputMatrix[row][column]=tempStore
	return inputMatrix


inputMatrix_5x5=[[1,2,3,4,5],
		[6,7,8,9,10],
		[11,12,13,14,15],
		[16,17,18,19,20],
		[21,22,23,24,25]]

inputMatrix_4x4=[[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]]
rotatedMatrix = rotateMatrixBy90(inputMatrix_5x5)
print("Rotated Matrix:\n",rotatedMatrix)
