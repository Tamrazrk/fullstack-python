class Farm:
    def __init__(self, owner):
        """creates an istance of Farm with name and empty animal list"""
        self.owner = owner
        self.animals = dict()

    def add_animal(self, animal, count=1):
        """adds animal with given count in animals"""
        if animal in self.animals:
            self.animals[animal] += count
        else:
            self.animals[animal] = count

    def get_info(self):
        """construct info string and return"""
        info_string = f"{self.owner}'s farm\n\n"
        for animal, count in self.animals.items():
            info_string += f"{animal} : {count}\n"
        return info_string


# Example
macdonald = Farm("McDonald")
macdonald.add_animal("cow", 5)
macdonald.add_animal("sheep")
macdonald.add_animal("sheep")
macdonald.add_animal("goat", 12)
print(macdonald.get_info())
