import random
from ex2 import Dog


class PetDog(Dog):
    def __init__(self, name, age, weight, trained):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *names):
        print(f"{', '.join(names + (self.name,))} all play together")

    def do_a_trick(self):
        if not self.trained:
            return

        tricks = [
            f"{self.name} does a barrel roll",
            f"{self.name} stands on his back legs",
            f"{self.name} shakes your hand",
            f"{self.name} plays dead"
        ]
        print(random.choice(tricks))


if __name__ == '__main__':
    dog = PetDog("Kitana", 3, 27, False)
    dog.train()
    dog.play("Rex", "Jax")
    dog.do_a_trick()
