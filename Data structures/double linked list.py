class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
        self.prev=None
class DoubleLinkedList:
    def __init__(self, value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def print_list(self):
        temp=self.head
        while temp is not None:
            print("<=", temp.value,"=>", end=' ')
            temp=temp.next
    def append(self, value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
        return True

    def pop(self):
        if self.tail==None:
            return None
        popped_node=self.tail
        self.length-=1
        if self.length == 0:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None
            popped_node.prev=None
        return popped_node

    def prepend(self, value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length +=1
        return True

    def pop_first(self):
        if self.head is None:
            return None
        popped_node=self.head
        if self.length == 1:
            self.head=None
            self.tail=None
        else:
            self.head=popped_node.next
            self.head.prev=None
            popped_node.next=None
        self.length -= 1
        return popped_node

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length/2:
            temp=self.head
            for _ in range(index):
                temp=temp.next
        else:
            temp=self.tail
            for _ in range(self.length-index-1):
                temp=temp.prev
        return temp

    def set(self, index, value):
        selected_node=self.get(index)
        if selected_node is None:
            return False
        selected_node.value=value
        return True

    def insert(self, index, value):
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        temp=self.get(index)
        before=temp.prev
        new_node=Node(value)
        before.next=new_node
        new_node.prev=before
        new_node.next=temp
        temp.prev=new_node
        self.length+=1
        return True

    def remove(self, index):
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        selected_node=self.get(index)
        if selected_node is None:
            return False
        before=selected_node.prev
        after=selected_node.next
        selected_node.next=None
        selected_node.prev=None
        before.next=after
        after.prev=before
        self.length-=1
        return True

x=DoubleLinkedList(4)
x.append(5)
x.append(6)
x.append(7)
x.append(8)
x.set(5, 10)
print("length: ", x.length)
x.print_list()
print()
x.remove(5)
print("length: ", x.length)
x.print_list()

