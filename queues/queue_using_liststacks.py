class Queue:
    def __init__(self):
        self.s1 = [] # s1 for inserting
        self.s2 = [] # s2 for copying over and reversing to remove.
    
    def enqueue(self, value):
        self.s1.append(value)
    
    def dequeue(self):
        self.peek()
        return self.s2.pop()
        
    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
            return self.s2[-1]
        else:
            return self.s2[-1]
    
    def empty(self):
        if not self.s2:
            if not self.s1:
                return True
            else:
                return False
        else:
            return False

if __name__ == "__main__":
    queue = Queue()
    print(queue.enqueue(4))
    print(queue.enqueue(5))
    print(queue.enqueue(6))
    print(queue.peek())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.enqueue(7))
    print(queue.peek())
    print(queue.empty())