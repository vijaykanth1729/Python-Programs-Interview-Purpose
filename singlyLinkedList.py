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

    # insertion at head position..
    def insertHead(self, newNode):
        temporary_node = self.head
        self.head = newNode
        newNode.next = temporary_node
        del temporary_node

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        # head->john->puppy-None
        if self.head is None:
            print("List is empty..")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next


firstNode = Node('John')
secondNode = Node('Puppy')
thirdNode = Node('Rambo')
fourthNode = Node('MyHead')
linkedlist = LinkedList()
linkedlist.insert(firstNode)
linkedlist.insert(secondNode)
linkedlist.insert(thirdNode)
linkedlist.insertHead(fourthNode)
linkedlist.printList()
