# binary search tree is a binary tree (child 0/1/2 nodes, child has one parent) and
# also a condition where childs are > to the right and < to the left. 
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        node = Node(value)
        if not self.root:
            self.root = node
        else:
            currentNode = self.root
            while True:
                if value > currentNode.value:
                    if currentNode.right:
                        currentNode = currentNode.right
                    else:
                        currentNode.right = node
                        return self
                elif value < currentNode.value:
                    if currentNode.left:
                        currentNode = currentNode.left
                    else:
                        currentNode.left = node
                        return self
        
    def lookup(self,value):
        currentNode = self.root
        if not self.root:
            return False
        while currentNode:
            if value > currentNode.value:
                currentNode = currentNode.right
            elif value < currentNode.value:
                currentNode = currentNode.left
            else:
                return True
        return False
    
    def remove(self,value):
        # node is a leaf
        # node has only 1 child
        # node has 2 childs
        # node not found. 
        currentNode = self.root
        currentNodeParent = None
        while (currentNode):
            if value > currentNode.value:
                currentNodeParent = currentNode
                currentNode = currentNode.right
            elif value < currentNode.value:
                currentNodeParent = currentNode
                currentNode = currentNode.left
        if currentNode.value == value:
            if not currentNode.right and not currentNode.left: # node is a leaf, no children.
                if currentNodeParent.right.value == value:
                    currentNodeParent.right = None
                else:
                    currentNodeParent.left = None
            elif not currentNode.right or not currentNode.left: # 1 child.
                if currentNode.right:
                    if currentNodeParent.right.value == value:
                        currentNodeParent.right = currentNode.right
                    else:
                        currentNodeParent.left = currentNode.right
                else:
                    if currentNodeParent.right.value == value:
                        currentNodeParent.right = currentNode.left
                    else:
                        currentNodeParent.left = currentNode.left
            else: # 2 children. # find right tree min and then remove the duplicate.
                self.min(currentNode.right)

    def min()
                





if __name__ == "__main__":
    