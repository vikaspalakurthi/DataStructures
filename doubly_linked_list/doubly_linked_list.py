class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    

class DoublyLinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node

    # append
    def append(self, value):
        node = Node(value)
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
    
    # prepend
    def prepend(self, value):
        node = Node(value)
        self.head.prev = node
        node.next = self.head
        self.head = node

    # printlist
    def printlist(self):
        list = []
        node = self.head
        while node.next is not None:
            list.append(node.value)
            node = node.next
        list.append(self.tail.value)
        return list

    # lookup/traverse_to
    def lookup(self, index):
        tempIndex = 0
        node = self.head
        while (tempIndex != index):
            node = node.next
            tempIndex += 1
        return node

    # insert
    def insert(self, value, index):
        node = self.lookup(index-1)
        newNode = Node(value)
        node.next.prev = newNode
        newNode.prev = node
        newNode.next = node.next
        node.next = newNode
        
    # remove
    def remove(self, index):
        leader = self.lookup(index-1)
        follower = leader.next # follower is the one that needs to be removed. 
        leader.next = follower.next
        if follower.next is not None:
            follower.next.prev = leader
        else:
            self.tail = leader


dll = DoublyLinkedList(0)
print(f"This is my first doubly linked list {dll.head.value}")

dll.append(1)
print(f"This is the doubly linked list after 1st append {dll.head}")

dll.append(2)
dll.append(3)
dll.append(4)

print(dll.lookup(0).value)

dll.insert(7,3)
dll.remove(5)

print(dll.printlist())

# node = Node(2)
# print(f"here is the node {node.value}")