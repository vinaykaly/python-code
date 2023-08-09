"""Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's."""
matrix = [[1,1,1],[1,0,1],[1,1,1]]

Index = []  #storing position of the zeros


for i in range(len(matrix)): #to know the position of the zeros in  matrix

    if 0 in matrix[i]:
        

        for k,j in enumerate(matrix[i]):
            x = []
            if j == 0:
                x = x+[i,k]

                Index.append(x) 
                """[1, 1]"""

for i,j in Index:

    for k in range(len(matrix)):
        if k == i:
            Len = len(matrix[k])
            matrix[k] = [0]*Len

        else:
            matrix[k][j] = 0

print(matrix) #Output: [[1,0,1],[0,0,0],[1,0,1]]
