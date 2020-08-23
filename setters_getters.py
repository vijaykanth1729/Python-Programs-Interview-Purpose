class Sample:
    def __init__(self, number=0):
        self.var = 10
        self._var = 20
        self.__var = 30
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def setters(self, value):
        self.__var = value

    def display(self):
        print("Executing display method")
        print(self.var, self._var, self.__var)

    def __display(self):
        '''private method'''
        print(self.__var)

    def getters(self):
        ''' you can access the private variable only using this method'''
        return self.__var

    def access_private_method(self):
        print("This is a private method...Accessible using setters.")
        return self.__display()

if __name__ == '__main__':
    s = Sample()
    #s = Sample(20)
    # s1 = Sample(25)
    #print(s+s1)
    s.display()
    # print(s.__var) not possible to access this, as it is a private data..
    # s.__display() not accessible outside the class as it is a private method
    print(s.getters())  # This is allowed..

    s.setters(5000) # this is possible to set a value..
    #s.__var = 1000  not possible to set a class variable value without setters.
    print(s.getters())
    s.access_private_method()  # this is possible
