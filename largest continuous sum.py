# given an array of integers +ve and -ve find the largest continuous sum?

arr = [1,2,-1,3,4,10,10,-10,-1]  # time complexity ---> O(n)
                                 # space complexity ---> O(1)  Date --> 26-10-2023

max_sum = current_sum = x[0]

for i in arr[1::]:

  current_sum = max(current_sum+i,i)
  max_sum = max(max_sum,current_sum)

print(max_sum)

