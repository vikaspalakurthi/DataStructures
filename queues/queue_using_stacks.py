# common interview question
# Logic: Queue is FIFO and Stack is LIFO,
# Stack does the push and pop on the same side. 
# Queue does the push at the rear end the pop at the front. 
# To implement Queue using 2 stacks, below is the logic: 
# For push, will just use stack.push into say s1., this for a stack would look like we are pushing on top. 
# If we pop now, it will be like removing the most recent element which is not a  queue behavior. 
# To imitate queue behavior, First we reverse the order of elements pushed into stack -> which technically mean we are removing elements from the other end 
# which is a required behavior for queue. 
from stacks import Stack

class Queue:
    def __init__(self):
        # stack2 -> going to be used for queue pops. after inserting from s1 reversing the push order.
        self.s2 = Stack()
        # stack1 -> going to be used for queue inserts.
        self.s1 = Stack()
    
    def enqueue(self, value):
        return self.s1.push(value) # stack push
    
    def dequeue(self):
        self.peek()
        return self.s2.pop() # stack pop
    
    def peek(self):
        if self.s2.isEmpty():
            while not self.s1.isEmpty():
                self.s2.push(self.s1.pop())
            return self.s2.peek()
        else:
            return self.s2.peek()
    
    def empty(self):
        if self.s2.isEmpty():
            if self.s1.isEmpty():
                return True
        else:
            return False

if __name__ == "__main__":
    queue = Queue()
    print(queue.enqueue(1))
    print(queue.enqueue(2))
    print(queue.enqueue(3))
    print(queue.peek())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.enqueue(4))
    print(queue.peek())


