class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, data):
        self.items.insert(0, data)

    def dequeue(self):
        self.items.pop()

    def printQueue(self):
        return self.items

    def queueLenght(self):
        return len(self.items)
if __name__ == '__main__':
    q = Queue()
    print(q.isEmpty())
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.printQueue())
    q.dequeue()
    print(q.printQueue())
    print("Queue Length: ", q.queueLenght())
