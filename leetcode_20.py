#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

def valid(a):

  stack = []
  opening = list("{[(")
  matching = list((('[',']'),('(',')'),('{','}')))

  if len(a)%2 == 0:

    for i in a:
      if i in opening:
         stack.append(i)
        
      else:
          if len(stack) == 0:
              return False
          y = stack.pop()

          if (y,i) not in matching:
              return False
    return len(stack)==0
  return False

print(valid("()[]{"))


  

  
