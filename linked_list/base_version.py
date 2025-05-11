class LinkedList:
    def __init__(self, value):
        self.head = {
            'value': value,
            'next': None
        }
        self.tail = self.head
        self.length = 1
    
    def append(self, value):
        self.tail['next'] = {
            'value': value,
            'next': None
        }
        self.length = self.length + 1
        self.tail = self.tail['next']
    
    def prepend(self, value):
        node = {
            'value': value,
            'next': self.head
        }
        self.head = node
        self.length += 1
    
    def printlist(self):
        # dont print it, return an array. 
        linkedListValues = []
        #print(f"this is the head {self.head} ")
        node = self.head
        #print(node['value'])
        linkedListValues.append(node['value'])
        while node['next'] is not None:
            node = node['next']
            linkedListValues.append(node['value'])
        return linkedListValues

    def insert(self, index, value):
        # write your code here.
        tempIndex = 0
        node = {
            'value': value,
            'next': None
        }
        tempNode = self.head
        if index == 0:
            node['next'] = self.head
            self.head = node
            self.length += 1
        else:
            while (tempIndex < index):
                if tempIndex == 0:
                    node['next'] = self.head['next']
                    tempNode = self.head
                else:
                    tempNode = tempNode['next'] # changing the node itself.
                    
                if tempIndex == index-1:
                    node['next'] = tempNode['next']
                    tempNode['next'] = node

                tempIndex += 1
        self.length += 1
                    
    def remove(self, index):
        # write your code here.
        tempNode = self.head # node 0. 
        tempIndex = 0
        while (tempIndex < index-1):
            tempNode = tempNode['next'] # tempIndex:0, tempnode: node1
            tempIndex += 1
            if tempIndex == index-1:
                tempNode['next'] = tempNode['next']['next']
            
            
        
    
    def lookup(self, index):
        # write your code here.
        return None

myLinkedList1 = LinkedList(10)
myLinkedList1.append(5)
myLinkedList1.append(16)
myLinkedList1.prepend(1000)
myLinkedList1.insert(3,4)
myLinkedList1.insert(2,2)

print(myLinkedList1.head)
print(myLinkedList1.tail)
print(myLinkedList1.length)

values = myLinkedList1.printlist()
print(values)

myLinkedList1.remove(2)
myLinkedList1.remove(3)
print(myLinkedList1.printlist())
