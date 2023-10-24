x = [1,2,1,2,3,4,3,2,1,2,3,4,5,65,6,5,4,3,3,2,1,3,3,4,5]

for  i in range(len(x)-1,-1,-1):
    for k in range(i):

        if  x[k] > x[k+1]:
            temp = x[k]

            x[k] = x[k+1]
            x[k+1] = temp

lower = 0
upper = len(x)-1
search = 65
while lower <= upper:
    mid = int((lower+upper)/2)

    if search == x[mid]:
        print("index",mid,sep="-->")
        break
    else:

        if x[mid] > search:
            upper = mid-1
        
        else:
            lower = mid+1

