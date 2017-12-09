class Parent(object):  # define parent class
    def myMethod(self):
        print("Calling Parent method")


class Child(Parent):  # define child class
    def meMethod(self):
        print("Calling child method")


c = Child()  # instance of child
c.myMethod()  # child calls overridden method
print(Child.__repr__)
