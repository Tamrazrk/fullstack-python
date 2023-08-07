import itertools


class Zoo:
    def __init__(self, zoo_name):
        """creates new instance with name and empty animals list"""
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        """adds new animal in animals list"""
        self.animals.append(new_animal)

    def get_animals(self):
        """prints all the animals in zoo"""
        print(self.animals)

    def sell_animal(self, animal_sold):
        """if animal_sold is in animals list it will be removed from it"""
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print("animal not found in zoo")

    def sort_animals(self):
        """groups animals with their first letter and returns resulting groups"""
        return itertools.groupby(sorted(self.animals), lambda x: x[0])

    def get_groups(self):
        """print all animals in groups"""
        groups = self.sort_animals()
        for _, group in groups:
            print(list(group))


ramat_gan_safari = Zoo("example_zoo")

ramat_gan_safari.add_animal("Lion")
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Elephant")
ramat_gan_safari.add_animal("Leopard")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Eagle")

print("All animals: ")
ramat_gan_safari.get_animals()

ramat_gan_safari.sell_animal("Giraffe")

print("\nGrouped animals:")
ramat_gan_safari.get_groups()
