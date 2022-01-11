class Node:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

class Tree:
    def __init__(self, value=None):
        if value==None:
            self.root=None
        else:
            self.root=Node(value)

    def insert(self, value):
        if self.root==None:
            self.root=Node(value)
        else:
            temp=self.root
            while temp is not None:
                if value < temp.value and temp.left is None:
                    temp.left=Node(value)
                    temp=None
                elif value > temp.value and temp.right is None:
                    temp.right=Node(value)
                    temp=None
                elif value < temp.value:
                    temp=temp.left
                elif value > temp.value:
                    temp=temp.right
                else:
                    return False
        return True

    def contain(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp=temp.left
            elif value > temp.value:
                temp=temp.right
            else:
                return True
        return False

    def min_value_node(self, current_node):
        while current_node.left is not None:
                current_node=current_node.left
        return current_node

tre=Tree()
tre.insert(47)
tre.insert(21)
tre.insert(76)
tre.insert(18)
tre.insert(27)
tre.insert(52)
tre.insert(82)
print(tre.min_value_node(tre.root.right).value)
