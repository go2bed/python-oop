""""Python deletes unneeded objects (built-in types or class instances) automatically
to free the memory space. The process by which Python periodically reclaims
blocks of memory that no longer are in use is termed Garbage Collection.

Python's garbage collector runs during program execution and is
triggered when an object's reference count reaches zero.
An object's reference count changes as the number of aliases that point to it changes.

An object's reference count increases when it is assigned
a new name or placed in a container (list, tuple, or dictionary).
The object's reference count decreases when it's deleted with del,
 its reference is reassigned, or its reference goes out of scope.
 When an object's reference count reaches zero, Python collects it automatically."""

a = 40  # Create object <40>
b = a  # Increase ref. count  of <40>
c = [b]  # Increase ref. count  of <40>

del a  # Decrease ref. count  of <40>
b = 100  # Decrease ref. count  of <40>
c[0] = -1  # Decrease ref. count  of <40>

"""You normally will not notice when the garbage collector destroys 
an orphaned instance and reclaims its space. 
But a class can implement the special method __del__(),
 called a destructor, that is invoked when the instance is about 
 to be destroyed. This method might be used to clean up any 
 non memory resources used by an instance."""


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")


pt1 = Point()
pt2 = pt1
pt3 = pt1
print(id(pt1), id(pt2), id(pt3))  # prints the ids of the obejcts
del pt1
del pt2
del pt3
