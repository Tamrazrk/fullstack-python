class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        dog1 = self.run_speed() * self.weight
        dog2 = other_dog.run_speed() * other_dog.weight
        winner_dog = None
        if dog1 > dog2:
            winner_dog = self
        elif dog2 > dog1:
            winner_dog = other_dog

        if winner_dog:
            return f"dog {winner_dog.name} won fight!"
        return "Draw"


if __name__ == "__main__":
    dogs = [
        Dog("Jax", 1, 15),
        Dog("Teacup", 2, 25),
        Dog("Rex", 1, 15)
    ]
    for dog in dogs:
        print(f"{dog.name}: {dog.bark()}, run speed: {dog.run_speed()}")

    print(dogs[1].fight(dogs[2]))
    print(dogs[2].fight(dogs[0]))


