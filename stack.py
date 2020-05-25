class stack:
  def __init__(self):
    self.stack=[]
  def isEmty(self):
    return self.stack==[]
  def push(self,data):
    self.stack.append(data)
  def pop(self):
    garbage=self.stack[-1]
    del self.stack[-1]
    return garbage 
  def peak(self):
    return self.stack[-1]
  def lengt_stack(self):
    return len(self.stack)       
  def print_stack(self):
   for x in range(len(self.stack)):
     print(self.stack[x])
s=stack()
s.push(4)
s.push(5)
s.print_stack()
print(s.pop())
s.print_stack()