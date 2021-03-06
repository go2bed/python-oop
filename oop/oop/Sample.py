class Sample(object):
    pass


x = Sample()

print(x)

print(type(x))


class Dog(object):
    # Class object Atribute
    species = 'mammal'
    ancestor = 'wolf'

    def __init__(self, breed, name, fur=True, paws=4, eyes=2):
        self.breed = breed
        self.name = name
        self.fur = fur
        self.paws = paws
        self.eyes = eyes

    def __hash__(self) -> int:
        return super().__hash__()


sam = Dog(breed='Lab', name='Jack', fur=False)

print(sam)
print(sam.__hash__())
print(sam.species)
print(sam.name)
print(sam.fur)
print(sam.ancestor)