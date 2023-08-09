"""Input: rowIndex = 3
Output: [1,3,3,1]
"""

res = [[1],[1,1]]
if rowIndex == 0 or rowIndex == 1:
    print(res[rowIndex])

else:
            
    z = [1,1]
    while True:
        y = 1
        x = [1,1]
        
        for i in list(range(len(res[len(res)-1])-1)):
            x.insert(y,z[i]+z[i+1])
            y = y+1

        res.append(x)
        z = x
        
        if len(res)-1 == rowIndex :
            print (res[rowIndex])
            break
