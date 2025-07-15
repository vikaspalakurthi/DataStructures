class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
    def enqueue(self,value):
        if self.length == 0:
            node = Node(value)
            self.last = node
            self.first = node
            self.length += 1
        else:
            node = Node(value)
            #Using a temp Node
            #holdingNode = self.last
            #self.last = node
            #holdingNode.next = self.last
            self.last.next = node
            self.last = node
            self.length += 1
        
        return self.last.value
    
    def dequeue(self):
        if self.length == 0:
            print("Queue already empty")
            return None
        else:
            #holdingNode = self.first
            self.first = self.first.next 
            self.length -= 1
            return self.first.value
    
    def peek(self):
        return self.first.value

my_queue = Queue()
print(my_queue.enqueue(1))
print(my_queue.enqueue(2))
print(my_queue.enqueue(3))
print(my_queue.enqueue(4))
print(my_queue.enqueue(5))
print(my_queue.enqueue(6))
print(my_queue.enqueue(7))
print(my_queue.dequeue())
print(my_queue.length)