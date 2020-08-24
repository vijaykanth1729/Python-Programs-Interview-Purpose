# single level inheritance...
class Apple:
    manufacturer = "Apple Inc."
    contactDetails = "www.apple.com/contact"

    @property
    def displayContactDetails(self):
        print("You can log on to our website, {}, to check more info".format(Apple.contactDetails))

    @staticmethod
    def dealersAvailble():
        print("Visit nearest branch to see avaialble dealers..")

class MacBook(Apple):
    def __init__(self):
        self.yearOfManufacture = 2020

    def manufacturerDetails(self):
        print("MacBook is manufactured in the year {} by {}".format
              (
                  self.yearOfManufacture, self.manufacturer
                  )
              )
macbook = MacBook()
macbook.manufacturerDetails()
macbook.displayContactDetails  # this is denoted as a property..
macbook.manufacturerDetails
macbook.dealersAvailble()

# python searches attribute in the order like,
# instance attributes, class attribute ->If not raises an error..
