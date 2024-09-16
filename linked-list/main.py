class Node:
    def __init__(self,data=None):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head

        while last.next is not None:
            last = last.next

        last.next = new_node

def __str__(self):
    ret_str = '['
    temp = self.head

    while temp is not None:
        ret_str += str(temp.val) + ','
        temp = temp.next

    ret_str = ret_str.rstrip(", ")
    ret_str += "]"

    return ret_str


LinkedList.__str__ = __str__

# node1 = Node(10)
l = LinkedList()
l.push(1)
l.push(2)
l.push(3)
print(l)