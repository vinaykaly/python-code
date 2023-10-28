x = "AAAABBBBCCCCCDDEEEE"

def string_compression(x):

  count = 1
  res = ""

  if len(x) == 1:
     return f"{x+str(count)}"
  if len(x) == 0:
     return x
    
  for i in range(1,len(x)):

      if x[i] == x[i-1]:
          count = count+1
      else:
          res = res+x[i-1]+f"{count}"
          count = 1
  res = res+x[i]+f"{count}"
  return res

print(string_compression(x))
  


          
      
     
    
  
  
