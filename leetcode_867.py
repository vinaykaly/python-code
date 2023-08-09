matrix = [[1,2,3],[4,5,6],[7,8,9]]

result = []
for i in range(len(matrix[0])):

    x = []

    for k in matrix:
        x.append(k[i])

    result.append(x)
print(result)
