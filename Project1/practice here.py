"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""
"""
class Classy(object):
    def __init__(self):
        self.items = []
    def addItems(self, item):
        self.items.append(item)
    def getClassiness(self):
        classiness_points = {"tophat": 2, "bowtie": 4, "monocle": 5}
        total_classiness = sum(classiness_points.get(item, 0) for item in self.items)
        return total_classiness

# Test cases
me = Classy()

# Should be 0
print (me.getClassiness())

me.addItem("tophat")
# Should be 2
print (me.getClassiness())

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print (me.getClassiness())

me.addItem("bowtie")
# Should be 15
print (me.getClassiness())"""

"""
# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

class Person:
    apples = 0
    ideas = 0


johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1


def exchange_apples(you, me):
    # Here, despite G.B. Shaw's quote, our characters have started with       #different amounts of apples so we can better observe the results.
    # We're going to have Martin and Johanna exchange ALL their apples with #one another.
    # Hint: how would you switch values of variables,
    # so that "you" and "me" will exchange ALL their apples with one another?
    # Do you need a temporary variable to store one of the values?
    # You may need more than one line of code to do that, which is OK.
    temp_apples = me.apples
    me.apples = you.apples
    you.apples = temp_apples
    return you.apples, me.apples


def exchange_ideas(you, me):
    # "you" and "me" will share our ideas with one another.
    # What operations need to be performed, so that each object receives
    # the shared number of ideas?
    # Hint: how would you assign the total number of ideas to
    # each idea attribute? Do you need a temporary variable to store
    # the sum of ideas, or can you find another way?
    # Use as many lines of code as you need here.
    org_you_ideas = you.ideas
    org_me_ideas = me.ideas
    you.ideas = org_me_ideas + me.ideas
    me.ideas = org_you_ideas + you.ideas
    return you.ideas, me.ideas


exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))
"""


"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

"""
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        #Get an element from a particular position.
        #Assume the first position is "1".
        #Return "None" if position is not in the list.
        current = self.head
        if position < 1:
            return None

        for i in range(1, position):
            if current is None:
                return None
            current = current.next
        return current

    def insert(self, new_element, position):
       #Insert a new node at the given position.
        #Assume the first position is "1".
        #Inserting at position 3 means between
        #the 2nd and 3rd elements.
        if position == 1:
            new_element.next = self.head
            self.head = new_element
        else:
            prev_element = self.get_position(position - 1)
            if prev_element is None:
                print("Invalid Position. Enter a valid position")
                return

            new_element.next = prev_element.next
            prev_element.next = new_element

    def delete(self, value):
        #Delete the first node with a given value.
        current = self.head
        if current is None:
            return
        if current.value == value:
            self.head = current.next
            return
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print
ll.head.next.next.value
# Should also print 3
print
ll.get_position(3).value

# Test insert
ll.insert(e4, 3)
# Should print 4 now
print
ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print
ll.get_position(1).value
# Should print 4 now
print
ll.get_position(2).value
# Should print 3 now
print
ll.get_position(3).value"""

