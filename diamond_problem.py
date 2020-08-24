'''
    A

B       C
    D
'''

'''
MRO (method resolution order) rule tells that if a method is not available in class d,
then it verifies the method in class B, if not available
then it checks in class C.
in this case, class B method is executed..
'''

class A:
    def method(self):
        print("This is method from class A")
class B(A):
    def method(self):
        print("This is method from class B")
class C(A):
    def method(self):
        print("This is method from class C")
class D(B, C):
    # def method(self):
    #     print("This is method from class D")
    pass
d1 = D()
d1.method()
