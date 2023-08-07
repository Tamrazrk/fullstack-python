from random import randint


class MyList:
    def __init__(self, letters):
        """Create new instalce of MyList with letters"""
        self.letters = letters

    def reverse(self):
        """return reversed list of letters"""
        return list(reversed(self.letters))

    def sort(self):
        """return sorted list of letters"""
        return sorted(self.letters)

    def generate_random_numbers(self):
        """
        generates new list of random numbers in range [-100, 100]
        with same length as current instace letters
        """
        return [randint(-100, 100) for _ in range(len(self.letters))]


# Example
mylist = MyList(["a", "b", "c", "e", "d"])
print("mylist:", mylist.letters)
print("reversed:", mylist.reverse())
print("sorted:", mylist.sort())
print("random numbers:", mylist.generate_random_numbers())
