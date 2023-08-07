import random


class Mutable:
    def mutate(self):
        """should be implemented"""
        pass

    def is_unit(self):
        """should be implemented"""
        pass

    def display(self):
        """should be implemented"""
        pass


class MutableSequence(Mutable):
    def __init__(self, sequence):
        """sequence is the list of objects that has .mutate() implemented itself"""
        self.sequence = sequence

    def mutate(self, probability=0.5):
        """mutate elements of sequence with given probability"""
        for element in self.sequence:
            if random.random() < probability:
                element.mutate()

    def is_unit(self):
        """returns True if all of it's elements are unit"""
        for element in self.sequence:
            if not element.is_unit():
                return False
        return True

    def display(self):
        for element in self.sequence:
            element.display()


class Gene(Mutable):
    def __init__(self, value):
        self.value = value

    def mutate(self):
        self.value = 1 - self.value

    def is_unit(self):
        return self.value == 1

    def display(self):
        print(self.value, end="")


class Chromosome(MutableSequence):
    def __init__(self, sequence):
        for element in sequence:
            if not (isinstance(element, Gene)):
                raise TypeError("Chromosome should consist of Genes")
        super().__init__(sequence)


class DNA(MutableSequence):
    def __init__(self, sequence):
        for element in sequence:
            if not (isinstance(element, Chromosome)):
                raise TypeError("DNA should consist of Chromosomes")
        super().__init__(sequence)


class Organism(Mutable):
    def __init__(self, dna, environment):
        self.dna = dna
        self.environment = environment

    def mutate(self):
        if random.random() < self.environment:
            self.dna.mutate()

    def is_unit(self):
        return self.dna.is_unit()

    def display(self):
        return self.dna.display()


if __name__ == "__main__":
    dna = DNA(
        [Chromosome([Gene(random.randint(0, 1)) for _ in range(10)]) for _ in range(10)]
    )

    org1 = Organism(dna, 0.5)

    iterations = 0
    while not org1.is_unit():
        org1.mutate()
        iterations += 1

    print("iterations:", iterations)
