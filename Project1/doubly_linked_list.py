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
            while n is not None:
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

ll2 = doublyLL()
ll2.print_LL_Reverse()