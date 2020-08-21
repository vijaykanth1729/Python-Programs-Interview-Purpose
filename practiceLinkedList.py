# create nodes
# create linked lists
# add nodes to linked lists..
# display the result..


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertHead(self, newNode):
        temporary_node = self.head
        self.head = newNode
        newNode.next = temporary_node
        del temporary_node

    def insert(self, newNode):
        # head->john->ben->None
        if self.head is None:
            self.head = newNode
        else:
            # self.head.next = newNode  [not a proper assumption..]
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def insertAt(self, newNode, position):
        # head->10->20->None || 10-15-20->None || position = 1
        if position == 0:
            self.insertHead(newNode)
            return
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break

            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1

    def printList(self):
        # head->john->amal-raj-None
        if self.head is None:
            print("List is empty..")
            return
        current_node = self.head
        while True:
            if current_node is None:
                break
            print(current_node.data)
            current_node = current_node.next


first_node = Node("John")
linkedList = LinkedList()
linkedList.insert(first_node)
second_node = Node('Amal')
linkedList.insert(second_node)
third_node = Node('Raj')
linkedList.insert(third_node)
fourth_node = Node("MyHead")
linkedList.insertHead(fourth_node)
fifth_node = Node("Iam at position 1")
linkedList.insertAt(fifth_node, 1)
linkedList.printList()
