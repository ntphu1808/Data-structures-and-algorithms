class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.length=1

    def print_stack(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    
    def push(self, value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        return True

    def pop(self):
        if self.head is None:
            return None
        temp=self.head
        self.head=self.head.next
        temp.next=None
        self.length-=1
        return temp

class Queue:
    def __init__(self, value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def print_queue(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    
    def enqueue(self, value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
        return True

    def dequeue(self):
        if self.head is None:
            return None
        node=self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head=self.head.next
            node.next=None
        self.length -=1
        return node

q=Queue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print("length: ", q.length, " and:")
q.print_queue()
b= q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()

q.enqueue(1)
q.enqueue(5)
print("b: ", b.value, " and length: ", q.length)
q.print_queue()