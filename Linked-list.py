class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self, value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def print_list(self):
        current_node=self.head
        while current_node is not None:
            print(str(current_node.value) + '->', end=' ')
            current_node=current_node.next

    def append(self, value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
        return True

    def pop(self):
        if self.head==None: return None
        temp=self.head
        pre=temp
        while temp.next is not None:
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
        return temp
    
    def prepend(self, value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        else:    
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        return True

    def pop_first(self):
        if self.head==None:
            return None
        old_head=self.head
        self.head=self.head.next
        self.length-=1
        if self.length==0:
            self.tail=None
        old_head.next=None
        return old_head
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp=self.head             
        for _ in range(index):     #we use underscore because inside the loop we don't use any variables, so just use underscore for the iteration.
            temp=temp.next
        return temp

    def set(self, index, value):
        selected_node=self.get(index)
        if selected_node is None:
            return False
        selected_node.value=value
        return True

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index==0:
            return self.prepend(value)
        if index==self.length:
            return self.append(value)
        new_node=Node(value)
        prev=self.get(index-1)
        new_node.next=prev.next
        prev.next=new_node
        self.length+=1
        return True

    def remove(self, index):
        if index<0 or index >= self.length:
            return False
        if index==0:
            return self.pop_first()
        if index==self.length-1:
            return self.pop()
        prev=self.get(index-1)
        removed_node=prev.next
        prev.next=removed_node.next
        removed_node.next=None
        self.length-=1
        return removed_node

    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        before=None
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after
        return True

li=LinkedList(1)
li.append(2)
li.append(3)
li.append(4)
li.append(5)
li.print_list()
print()
li.reverse()
li.print_list()
