class Stack:
    def __init__(self):
        self.list = []

    def push(self,value):
        self.list.append(value)
        return self.list
    
    def pop(self):
        self.list.pop()
        return self.list
    
    def peek(self):
        return self.list[-1]


stack1 = Stack()
print(stack1.push("google"))
print(stack1.push("udemy"))
print(stack1.push("discord"))
print(stack1.pop())
print(stack1.peek())