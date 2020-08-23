class Stack(object):

    def __init__(self):
        self.item = []

    def push(self, data=''):
        '''
        pushing an element to the stack..
        '''
        self.item.append(data)

    def pop(self):
        '''
        pop an element from Stack
        '''
        self.item.pop()
    def isempty(self):
        if len(self.item)>0:
            print("Your stack is not empty..")
        else:
            print("You dont have any items in your stack.")
    def peek(self):
        if self.item:
            return self.item[-1]
        else:
            print("No items present")
    def stack_size(self):
        if self.item:
            print("Current stack size is: ", len(self.item))
        else:
            print("Zero")
    def display_stack(self):
        print(self.item)
if __name__ == '__main__':
    s1 = Stack()
    s1.push(2)
    s1.push(200)
    s1.push(300)
    s1.isempty()
    s1.stack_size()
    s1.display_stack()
    s1.pop()
    s1.display_stack()
    print(s1.peek())
    s1.stack_size()
