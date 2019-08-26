class Animal:
    def __init__(self):
        print('Animal constructor')
        self.age = 1

    def eat(self):
        print('eat')


class Mammal(Animal):
    def __init__(self):
        super().__init__() #super is adding to the init methos in the animal class instead of overrriding
        print('Mammal constructor')
        self.weight = 2

    def walk(self):
        print('walk')


dog = Mammal()
print(dog.age)
print(dog.weight)

