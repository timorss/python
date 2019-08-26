class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print('eat')


class Mammal(Animal):
    def walk(self):
        print('walk')


class Fish(Animal):
    def swim(self):
        print('swim')


fish = Fish()
fish.eat()
print(fish.age)
print(isinstance(fish, Fish))  # True
print(isinstance(fish, Animal))  # True
print(issubclass(Fish, Animal))  # True
