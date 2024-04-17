# Class is define with a capital letter beginning in order to differentiate it from variables
class Dog:
    def __init__(self, name):
        self.name = name
        self.legs = 4
    def speak(self):
        self.name + ' says: Bark!'

my_dog = Dog('Rover')
another_dog = Dog('Fluffy')
my_dog.speak()
another_dog.speak()


