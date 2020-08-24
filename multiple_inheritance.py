class OperatingSystem:
    multitasking = True
    name = "MAC OS"

class Apple:
    website = "www.apple.com"
    name = "Apple"

class MacBook(OperatingSystem, Apple):
    def __init__(self):
        if self.multitasking is True:
            print(
            "MacBook is a multitasking \
operating system, visit {} for more info".format(self.website)
            )
            print(self.name)

macbook = MacBook()
