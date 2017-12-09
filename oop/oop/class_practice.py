class Name(object):
    'Optional class documentation string'
    name_counter = 0  # Class  variable that is shared by all instances of a class. like static in Java

    def __init__(self):
        Name.name_counter += 1


name = Name()
nema1 = Name()

print(
    "#Name.name_counter  Will print '2' because we have"
    " two instances of class Name and we have +=1 in initialization method")
print(Name.name_counter)


print("# Adding an 'name' attribute to the Name class.")
name.value = 'Sara'  # Add an 'name' attribute to the Name class.

print(name.value)
print('\n')

print('modified value of the value attribute')
name.value = 8  # Modify 'name' attribute.
print(name.value)

del name.value  # Delete 'name' attribute. and after this statement
#  we cannot call print(name.value) - it would be error caused
print("this will print 'Optional class documentation string''\n")
print(Name.__doc__)  # this will print 'Optional class documentation string'

print('\n Instead of using the normal statements to access attributes, '
      'you can use the following functions −')
print("# Returns true if 'age' attribute exists")
print(hasattr(name, 'age'))

print("# Set attribute 'age' at 8")
setattr(name, 'age', 8)

print("# Returns value of 'age' attribute")
print(getattr(name, 'age'))

print("# Deleting attribute 'age'")
delattr(name, 'age')
