class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
        self.prev=None

class doublyLL:
    def __init__(self):
        self.head=None
    def print_LL(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data, end=" ")
                n = n.ref
            print()

    def print_LL_Reverse(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            while n is not None:
                print(n.data, end=" ")
                n = n.prev
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty!")
    def insert_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.ref = self.head
            self.head.prev = new_node
            self.head = new_node
    def insert_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
            new_node.prev = n

ll2 = doublyLL()

ll2.insert_end(50)
ll2.insert_begin(10)
ll2.insert_end(23)
ll2.insert_end(100)
ll2.insert_begin(199)
ll2.print_LL()
ll2.print_LL_Reverse()