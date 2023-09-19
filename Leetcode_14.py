"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string ."""

strs = ["flower","flow","flight"]

Min = min([len(i) for i in strs])  

result = ""

for i in range(Min):

    Set = set({})

    for k in strs:

       Set.add(k[i])

   if len(Set) > 1 :
     print(result)
     break

   else:
       result = result + k[i]



"""                                                            OR                                               """
strs = ["flower","flow","flight"]

result = ""

for i in zip(*strs):

    if len(set(i)) == 1:
          result = result + i[0]

    else:
      print(result)
      break
  
