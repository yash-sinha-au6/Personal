class Node:
  def __init__(self,name):
    self.name=name
    self.adj_list=[]
    self.visited=False
class Breath_search_first:
  def bfs(self,startnode):
     queue=[]
     queue.append(startnode)
     startnode=True
     while queue:
        actualnode= queue.pop(0)
        print(actualnode.name)
        for i in actualnode.adj_list:
          if not i.visited:
            i.visited=True
            queue.append(i)
n1=Node("B")
n2=Node("C")
n3=Node("A")
n4=Node("E")
n5=Node("F")
n6=Node("L")
n7=Node("k")
n1.adj_list.append(n2)
n1.adj_list.append(n2)
n1.adj_list.append(n3)
n2.adj_list.append(n4)
n2.adj_list.append(n7)
n3.adj_list.append(n6)
n3.adj_list.append(n5)

bfs=Breath_search_first()
bfs.bfs(n1)           
