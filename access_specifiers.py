# public => memberName   # accessible to all classes and outside classess
# protected => _memberName # accesible to class and its child classes, but no restriction
# private => __memberName # accessible only in the same class, not even for child classess
# still private is not restricted ,, you can access using  (_className__memeberName)
class Car:
    numberOfWheels = 4
    _color = 'black'
    __yearOfManufacturer = 2020
class Bmw(Car):
    def __init__(self):
        print("Bmw consist of {} wheels and its color is {}".format(self.numberOfWheels, self._color))
c = Car()
bmw = Bmw()
#print("This car is manufactured in the year: ".format(c.__yearOfManufacturer))
print("This car is manufactured in the year: {}".format(c._Car__yearOfManufacturer))
#print(c._color)->Accessible..
