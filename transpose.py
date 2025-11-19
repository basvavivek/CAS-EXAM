def transpose_matrix(matrix):
    transpose=[[row[i] for row in matrix] for i in range(len(matrix[0]))]
    return transpose
matrix=[[1,2],[3,4],[5,6]]
result=transpose_matrix(matrix)
print(result)