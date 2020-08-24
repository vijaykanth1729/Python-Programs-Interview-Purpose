class Employee:

    def setNumberOfWorkingHours(self):
        self.workingHours = 40

    def displayNumberOfWorkingHours(self):
        print(self.workingHours)


class Trainee(Employee):

    def setNumberOfWorkingHours(self):
        self.workingHours = 45

    def resetNumberOfWorkingHours(self):
        super().setNumberOfWorkingHours()

e1 = Employee()
e1.setNumberOfWorkingHours()
print("Number of working hours of employee: ", end=' ')
e1.displayNumberOfWorkingHours()
t1 = Trainee()
t1.setNumberOfWorkingHours()
print("Number of working hours of Trainee: ", end=' ')
t1.displayNumberOfWorkingHours()
t1.resetNumberOfWorkingHours()
print("Number of  RESET working hours of Trainee: ", end=' ')
t1.displayNumberOfWorkingHours()


# class A:
#     name = "bmw"
#     def __init__(self,age):
#         self.age = age
#     def display(self):
#         print("hello world..")
# class B(A):
#     def __init__(self):
#         self.age = 2000
#     def display(self):
#         super().display()
#         super().__init__(300)
#         print(self.age)
#
#
# b1 = B()
# b1.display()
