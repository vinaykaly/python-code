#Valid Anagram 16-10-2023

def anagram(s,t):

   x = s.replace(" ","").lower()
   y = t.replace(" ","").lower()

   return sorted(x) == sorted(y)

print(anagram("dog","god"))
