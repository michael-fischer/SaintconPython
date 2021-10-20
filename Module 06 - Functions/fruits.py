class Fruit:
    name = 'Fruits'

    @classmethod
    def printName(cls):
        print('the name of the class is: ', cls.name)

class NotFruit:
    name = 'Not a Fruit'


Fruit.printName()      # prints Fruits
Fruit.printName(NotFruit)   # Throws a type error as an extra parameter was passed
