#create nodes, create LinkedLists, add nodes to linkedlIsts, then print data
# each node contains Data, next pointer (which initially points to None)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def listLength(self):
        currentNode = self.head
        count = 1
        while currentNode.next is not None:
            currentNode = currentNode.next
            count+=1
        return count

    def insertHead(self, newNode):
        # trying to insert at head position..
        # now we need to store the current Head position in a tem variable
        # and add self.head to newNode
        # Now new node should point to temp node..
        tempNode = self.head
        self.head = newNode
        newNode.next = tempNode
        del tempNode

    def insertAt(self, newNode, position):
        #iamhead->john->ben->mathew->None
        # we need to insert newNode at position 1
        # traverse through position1, and store previous data in a temp variable
        # next add the next of previous to currentnODE.
        if position==0:
            self.insertHead(newNode)
            return
        if position > self.listLength():
            print("Invalid option")
            return
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position: # 0, 1
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition+=1



    def insertEnd(self, newNode):
        #John->None
        if self.head is None:
            self.head = newNode
        else:
            # Head->John->Ben->None
            #now by adding third node John points to mathew, which is False..
            #self.head.next = newNode  # not a proper solution..
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
    def deleteEnd(self):
        #head->iamhead->iampos1->john->ben-mathew-None
        # we need to remove matew...need to traverse till mathew,
        # if mathew.next is None then delete that node, and before doing
        # that store previous node in a varaiable and point that previousNode
        # variable next to None..
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next = None


    def printList(self):
        # head->john->ben->mathew->None
        if self.head is None:
            print("List is Empty")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next


firstNode = Node("John")
linkedlist = LinkedList()
linkedlist.insertEnd(firstNode) # initailly head is None, then insert that to a node
secondNode = Node("Ben")
linkedlist.insertEnd(secondNode)
thirdNode = Node("Mathew")
linkedlist.insertEnd(thirdNode)
headNode = Node("Iam head")
linkedlist.insertHead(headNode)
positionNode = Node("Iam at position1")
linkedlist.insertAt(positionNode, 1)
linkedlist.deleteEnd()
linkedlist.printList()
print("Length of linked List:",linkedlist.listLength())
