class Node:
  def __init__(self,name):
    self.name=name
    self.adj_list=[]
    self.visited=False

class depth_first_search:
  def dfs(self,startnode):
    stack=[]
    stack.append(startnode)
    startnode=True
    while stack:
      actualnode = stack[-1]
      stack.pop()
      print(actualnode.name)
      for i in actualnode.adj_list:
        if not i.visited:
          i.visited=True
        stack.append(i)
n1=Node("A")
n2=Node("C")
n3=Node("B")
n4=Node("D")  
n5=Node("E")
n1.adj_list.append(n2)
n1.adj_list.append(n3)
n2.adj_list.append(n4)
n3.adj_list.append(n5)
dfs=depth_first_search()
dfs.dfs(n1)    