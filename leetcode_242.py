#Valid Anagram 16-10-2023

def anagram(s,t): #n*log(n) Time comp

   x = s.replace(" ","").lower()
   y = t.replace(" ","").lower()

   return sorted(x) == sorted(y)

print(anagram("dog","god"))

#-------------------or----------------------

def anagram2(s,t):           # o(n) TC

   x = s.replace(" ","").lower()
   y = t.replace(" ","").lower()

   if len(x) == len(y):
      return False

   count = {}

   for i in x:

      if i not in count:

         count[i] = 1

      else:
         count[i] = count[i] + 1

   for i in y:
      if i in count:
         count[i] = count[i] - 1
      else:
         return False

   for i in count:

      if count[i] != 0:
         return False

   return True
   
         

   

print(anagram2("got","ogt"))
   

  
