from oop.Book import Book


class Dog(object):
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def area(self):
        return self.species

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


sam = Dog('Lab', 'Sam')
print(sam.breed)

sam.set_name('bublik')
print(sam.get_name())

book = Book("Python Rocks!", "Jose Portilla", 159)
print(book)
