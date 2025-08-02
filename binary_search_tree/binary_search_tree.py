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
    
    # def remove(self,value):
    #     # node is a leaf
    #     # node has only 1 child
    #     # node has 2 childs
    #     # node not found. 
    #     currentNode = self.root
    #     currentNodeParent = None
    #     while (currentNode):
    #         if value > currentNode.value:
    #             currentNodeParent = currentNode
    #             currentNode = currentNode.right
    #         elif value < currentNode.value:
    #             currentNodeParent = currentNode
    #             currentNode = currentNode.left
    #     if currentNode.value == value:
    #         if not currentNode.right and not currentNode.left: # node is a leaf, no children.
    #             if currentNodeParent.right.value == value:
    #                 currentNodeParent.right = None
    #             else:
    #                 currentNodeParent.left = None
    #         elif not currentNode.right or not currentNode.left: # 1 child.
    #             if currentNode.right:
    #                 if currentNodeParent.right.value == value:
    #                     currentNodeParent.right = currentNode.right
    #                 else:
    #                     currentNodeParent.left = currentNode.right
    #             else:
    #                 if currentNodeParent.right.value == value:
    #                     currentNodeParent.right = currentNode.left
    #                 else:
    #                     currentNodeParent.left = currentNode.left
    #         else: # 2 children. # find right sub tree min and then remove the duplicate.
    #             # node to be deleted has 2 childs. 
    #             rightMinNode = self.min(currentNode.right)
    #             if currentNodeParent.right.value == value:
    #                 currentNodeParent.right.value = rightMinNode.value
    #                 self.remove(rightMinNode.value)
    #             else:
    #                 currentNodeParent.left.value = rightMinNode.value
    #                 self.remove(rightMinNode.value)
                
    def min(self, node: Node):
        min = node.value
        while node.left:
            node = node.left
        return node
    
    def breadthFirstSearch(self):
        currentNode = self.root
        #        9
        #   4        20
        # 1   6   15    170
        list = []
        queue = []
        queue.append(currentNode)
        while queue:
            currentNode = queue.pop(0)
            list.append(currentNode.value)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        return list
    
    def breadthFirstSearchRecursive(self, queue, list):
        if not queue:
            return list
        currentNode = queue.pop(0)
        list.append(currentNode.value)
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
        
        return self.breadthFirstSearchRecursive(queue, list)
    
    def traverseInOrder(self, tree, list):
        if not tree.left and not tree.right:
            list.append(tree.value)
            return list
        if tree.left:
            self.traverseInOrder(tree.left, list)
        list.append(tree.value)
        if tree.right:
            self.traverseInOrder(tree.right,list)
        
        return list

    def DFSInOrder(self):
        return self.traverseInOrder(self.root, [])
    
    def DFSPostOrder(self):
        return self.traversePostOrder(self.root, [])

    def traversePostOrder(self, tree, list):
        if not tree.left and not tree.right:
            list.append(tree.value)
            return list

        if tree.left:
            self.traversePostOrder(tree.left, list)
        if tree.right:
            self.traversePostOrder(tree.right, list)
        list.append(tree.value)

        return list

    def DFSPreOrder(self):
        return self.traversePreOrder(self.root, [])

    def traversePreOrder(self, tree, list):
        if not tree.left and not tree.right:
            list.append(tree.value)
            return list
        
        list.append(tree.value)
        if tree.left:
            self.traversePreOrder(tree.left, list)
        if tree.right:
            self.traversePreOrder(tree.right, list)
        
        return list



if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(9)
    tree.insert(4)
    tree.insert(20)
    tree.insert(1)
    tree.insert(170)
    tree.insert(15)
    tree.insert(6)
    print(tree.breadthFirstSearch())
    print(tree.breadthFirstSearchRecursive([tree.root], []))
    list1 = tree.DFSInOrder()
    list2 = tree.DFSPostOrder()
    list3 = tree.DFSPreOrder()
    print(f"In Order DFS: ${list1}")
    print(f"Post order DFS: ${list2}")
    print(f"Pre Order DFS: ${list3}")
    