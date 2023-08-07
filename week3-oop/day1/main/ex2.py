class Dog:
    def __init__(self, name, height):
        """creates new instance of Dog with name and height"""
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")


davids_dog = Dog("Rex", 50)
print(f"name: {davids_dog.name}, height: {davids_dog.height}")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print(f"name: {sarahs_dog.name}, height: {sarahs_dog.height}")
sarahs_dog.bark()
sarahs_dog.jump()

bigger_dog = davids_dog
if sarahs_dog.height > davids_dog.height:
    bigger_dog = sarahs_dog

print(f"bigger dog name is: {bigger_dog.name}")
