class Fruit:
    name = 'Fruits'

    def printName(cls):
        print('the name of the class is: ', cls.name)

class NotFruit:
    name = 'Not a Fruit'


Fruit.printName(Fruit)      # prints Fruits
Fruit.printName(NotFruit)   # prints Not a Fruit

