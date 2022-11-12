class Bee:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Bee {self.name} has a yellow-black color, 4 wings, 5 eyes and sting'

    def age_class(self):
        if 5 > self.age > 1:
            return 'This is a queen bee'
        elif self.age < 1:
            return 'This is a worker bee'
        else:
            'This bee is dead'

    def say(self):
        return f"Bee {self.name} says 'Bzzz'"


maya = Bee('Maya', 2)

