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
    #removing the Nodes from a linked list(beginning, middle, after)

    def remove_begin(self):
        if self.head is None:
            print("LList is empty so we cannot delete anything!")
            return
        else:
            self.head = self.head.ref


    def remove_last(self):
        if self.head is None:
            print("LList is empty so we cannot delete anything!")
            return
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def remove_any(self,x):
        if self.head is None:
            print("Cannot delete since LL is empty!")

        if x==self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("Invalid Node! Give a valid Input")
        else:
            n.ref = n.ref.ref









ll1 = Linked_list()
ll1.add_begin(10)
ll1.add_begin(23)
ll1.add_end(55)

ll1.add_begin(122)
ll1.print_ln()
ll1.remove_any(10)
#ll1.remove_last()
ll1.print_ln()