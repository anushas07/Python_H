class Programmer:
    company = "Microsoft"


    def __init__(self,name,product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the programmer in {self.company} is {self.name} and the product is {self.product}")


harry = Programmer("Harry","Skype")
riya = Programmer("Riya","Github")
harry.getInfo()
riya.getInfo()
