class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
  # method override of string method for the node
  def __str__ (self):
    return f'{self.data}'
class BinaryTree:
  def __init__(self):
    self.root = None
  def insert(self, data): #done
    '''
      Insert(data: any) -> None:\n 
      creates a new Node from the data passed in and adds it to the tree
      If the data is already in the tree, does not insert it again
    '''
    #first make a node from the data
    new_node = Node(data)
    # if there is no root, set node to be root
    if not self.root:
      self.root = new_node
      return
    # loop over the tree starting at root and do comparisons
    current_node = self.root
    while current_node:
      # if the data is smaller than the current node
      if new_node.data < current_node.data:
        # if there is no left
        if not current_node.left:
          # set the left to be the new node
          current_node.left = new_node
          return
        else: current_node = current_node.left
      # if the new node's data is bigger than the current node
      elif new_node.data > current_node.data:
        if not current_node.right:
          current_node.right = new_node
          return
        else: current_node = current_node.right
      else: return # return if duplicate
  def search(self, val):#done
    '''
      search(value: any) -> value or bool:\n 
      Performs depth first search
      Search the Tree for a node with the given value
      If the node exists, return it
      If the node doesn't exist, return false
    '''
    # check if the tree is empty
    if not self.root:
      return False
    # loop through the tree starting at the root
    current_node = self.root
    while current_node:
      # if the value is less than the current node
      if val < current_node.data:
        # set current node to be the left
        current_node = current_node.left
      # else if the value is greater
      elif val > current_node.data:
        # set current node to be the right
        current_node = current_node.right
      # else return the node
      else:
        return current_node
    return False
  def print(self, node=None): # done
    '''
      print(node=optional: Node) -> None:\n
      prints out all values recursively (in a breadth first search fashion)
      defualt start is at root node
    '''
    # check if this is the first recursion
    if not node: node = self.root
    # print the node
    print(node)
    # if there is a left node
    if node.left:
      # recursively invoke self.print on the node
      self.print(node.left)
    # if there is a right node
    if node.right:
      # recurse...
      self.print(node.right)
  def size(self, node=None): #done?
    '''
      size(node=optional: Node) -> int:\n 
      performs breadth first search
      Calculate the number of nodes in the tree, starting from the given node
      If no node is provided, we can use the root as a sensible default
    '''
    if not node:
      node = self.root
    count = 0
    def re_size(node):
      nonlocal count
      if node:
        count += 1
        re_size(node.left)
        re_size(node.right)
    re_size(node)
    return count
    
  def height(self, node=None):
    '''
      height(node=optional: Node) -> int:\n 
      perform breadth first search
      Calculate the maximum amount of nodes in any one path from the given node
      If not given a specific node, default to using the root node
    '''
    if not node:
      node = self.root
    max_height = 0
    def re_height(node, height = 1):
      nonlocal max_height
      if node:
        if height > max_height:
          max_height = height
        re_height(node.left, height + 1)
        re_height(node.right, height + 1)
    re_height(node)
    return max_height


  def get_max(self): #done
    '''
      getMax() -> int:\n 
      perform depth first search
      Calculate the maximum value held in the tree
    '''
    # check if tree is empty
    if not self.root:
      return None
    current_node = self.root
    while current_node.right:
      current_node = current_node.right
    return current_node.data
    
  def get_min(self): #done
    '''
      getMin() -> int:\n 
      perform depth first search
      Calculate the minimum value held in the tree
    '''
    if not self.root:
      return None
    current_node = self.root
    while current_node.left:
      current_node = current_node.left
    return current_node.data
   