def determinant(matrix):
	if len(matrix)!=2 or len(matrix[0])!=2 or len(matrix[1])!=2:
		raise ValueError("input matrix must be a 2*2 matrix")
	return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
matrix_2=[[1,2,[3,4]]
result=determinant(matrix_2)
print("Determinant of 2*2 matrix=",result)
