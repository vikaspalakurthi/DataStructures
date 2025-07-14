# Using singly Linked Lists
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.bottom = None
        self.top = None
        self.length = 0

    def push(self,value):
        node = Node(value)
        if self.length == 0:
            self.top = node
            self.bottom = node
        else:
            tempNode = self.top
            self.top = node
            self.top.next = tempNode
        self.length += 1
        return self.top.value

    def pop(self):
        if self.length == 0:
            return None
        else:
            self.top = self.top.next
            self.length -= 1
        return self.top.value

    def peek(self):
        return self.top.value


stack1 = Stack()
print(stack1.push("google"))
print(stack1.push("udemy"))
print(stack1.push("discord"))
print(stack1.pop())
print(stack1.peek())
print(stack1.length)