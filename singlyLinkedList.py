# create nodes..
# create linked list
# add nodes to linked list.

# node contains, data and next(initially next should be Empty.)
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # head is initially None
    def __init__(self):
        self.head = None




firstNode = Node('John')
linkedlist = LinkedList()
linkedlist.insert(firstNode)
