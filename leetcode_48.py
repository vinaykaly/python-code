


matrix = [[1,2,3],[4,5,6],[7,8,9]]

Len = len(matrix[0])
result = []
for i in range(Len):

     x = []
     for k in matrix:
          x.append(k[i])

     result.append(x[::-1])


print(result)
