class Node(object):

    def __init__(self,value):
        self.value =value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)
        
        
    def print_tree(self,traversal_type):
        
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_traversal(tree.root,"")
        else:
            return " Traversal type not supported"

    def preorder_print(self,start,traversal) -> object:
        """
        Root-> Left -> Right
        :param start: where the root node is to start traversing
        :param traversal: where the traversed data will be stored
        :return: a string of all the traversed data
        """
        if start :
            traversal += (str(start.value) + "->")
            traversal= self.preorder_print(start.left, traversal)
            traversal=  self.preorder_print(start.right, traversal)
        return traversal

    def inorder_traversal(self,start,traversal):

        if start:
            traversal=self.inorder_traversal(start.left, traversal)
            traversal += str(start.value + "->")
            traversal = self.inorder_traversal(start.right,traversal)
        return traversal
    
    def postorder_traversal(self,start,traversal):
        if start:
            traversal=self.inorder_traversal(start.left, traversal)
            traversal = self.inorder_traversal(start.right,traversal)
            traversal += str(start.value + "->")
        return traversal
    


            
#  1
#  /\
# 2  3
# /\
# 4 5
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)

tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print (tree.print_tree("preorder"))
