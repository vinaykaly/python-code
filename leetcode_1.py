
def two_sum(nums,target):    #O(n)  24/oct/23

  for i,j in enumerate(nums):

    k = target-j
    if j in nums:
      if i != nums.index(k):  #index = O(n)
        return (i,nums.index(k))

print(two_sum([3,3],6))
        

  
