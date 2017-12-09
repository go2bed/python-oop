class Book(object):
    def __init__(self, title, author, pages_umber):
        print('A book has been created!')
        self.title = title
        self.author = author
        self.pages_umber = pages_umber

    def __str__(self):
        return "Title: %s, Author: %s, pages %s " % (self.title, self.author, self.pages_umber)

    def __len__(self):
        return self.pages_umber

    def __del__(self):
        print(" A book i gone!")


b = Book('Python', 'Jose', 101)

print(b)
print(b.__len__())

del b  # After calling this method we could
# not print or use book anyway cause it's already has been deleted
# so print(b) will be cause of the error


