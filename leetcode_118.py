"""Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]"""

res = [[1],[1,1]]

if numRows == 1 or numRows == 2:
    print (res[:numRows])

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
        
        if len(res) == numRows:
            print (res)
  
       
