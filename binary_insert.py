class Node:
  def __init__(self,data):
    self.data=data
    self.leftchild=None
    self.rightchild=None
class binary_search_tree:
  def __init__(self):
    self.root=None
  def insert(self,data):
    if not self.root:
      self.root=Node(data)
    else:
      self.insertnode(data,self.root)
  
  def insertnode(self,data,node): #condition checking for left child and right child of norde
    if data < node.data:
      if node.leftchild:
        self.insertnode(data,node.leftchild)
      else:
        node.leftchild=Node(data)
    else:
      if node.rightchild:
        self.insertnode(data,node.rightchild)
      else:
        node.rightchild=Node(data)

  def minvalue(self):
    if self.root:
     return self.min(self.root) 
  def min(self,node):
    if node.leftchild:
      return self.min(node.leftchild)       
    return node.data
  def maxvalue(self):
    if self.root:
     return self.max(self.root)
  def max(self,node):
    if node.rightchild:
      return self.max(node.rightchild)
    return node.data
  def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.leftchild)
            print(node.data)
            self.inorder_traversal(node.rightchild)  

  def traverse(self):
    if self.root:
      self.traverseinorder(self.root)

  def traverseinorder(self,node):
    if node.leftchild:
       self.traverseinorder(node.leftchild) 

    print(node.data)

    if node.rightchild:
       self.traverseinorder(node.rightchild)
   

bst=binary_search_tree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(6)
bst.insert(4)
bst.insert(16)
bst.insert(14)
bst.traverse()

          