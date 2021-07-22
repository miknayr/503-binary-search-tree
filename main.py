from BinaryTree import Node
from BinaryTree import BinaryTree
# tester node
my_node = Node('hello')
# print(my_node)
my_BST = BinaryTree()
my_BST.insert(10)
# print(my_BST.root)
my_BST.insert(12)
my_BST.insert(8)
# print(my_BST.root.right)
# my_BST.print()
my_BST.insert(15)
my_BST.insert(9)
my_BST.insert(3)
my_BST.insert(21)
my_BST.insert(87)
print(my_BST.search(87))
print(my_BST.get_max([1,2,3,4,5]))