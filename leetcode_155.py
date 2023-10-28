class stack:         # time complexity --> O(1)

  def __init__(self):
    self.items = []
    self.min_stack = []
    
  def push(self,value):

    self.items.append(value)

    if not self.min_stack or value <= self.min_stack[-1]:
      self.min_stack.append(value)

  def pop(self):

    if self.items:
      if self.items[-1] == self.min_stack[-1]:
        self.min_stack.pop()
      self.items.pop()
      
  def  top(self):
    if self.items:
     return self.items[len(self.items)-1]

  def Min(self):
    if self.items:
     return self.min_stack[-1]



    
     
                                   
