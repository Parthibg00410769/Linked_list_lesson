#To traverse a Linked_list
#In this tutorial ref means next

class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class Linked_list:
    def __init__(self):
        self.head=None

    def print_ln(self):
        if self.head is None:
            print("Linked list is Empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,end= " ")
                n=n.ref
            print()
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref = new_node
    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x==n.data:
                break
            n = n.ref
        if n is None:
            print("Invalid input")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def add_before(self,data,x):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data==x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty!")




ll1 = Linked_list()
ll1.add_begin(10)
ll1.add_begin(23)
ll1.add_end(55)

ll1.add_begin(122)
ll1.print_ln()
ll1.add_after(69, 10)
ll1.add_before(555,69)
ll1.insert_empty(333)
ll1.print_ln()