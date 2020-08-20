'''
Linked List will hold the data and next address of a node.
eg: 6-->4-->2-->1
lets consider head = 6
head.data refers to First Node data i,e 6
head.next refers to the next node address, to get the data of it
we should use head.next.data  and so, on...
'''


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None  # lets conside initial next address is None..


def count_nodes(head):
    # assume head is not None..
    count = 1
    current = head
    while current.next is not None:
        current = current.next
        count += 1
    return count


nodeA = Node(6)
nodeB = Node(5)
nodeC = Node(4)
nodeD = Node(3)
nodeE = Node(2)
nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
print("This ilinked list length is:", )
print(count_nodes(nodeA))
