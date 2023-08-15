import random


def guess_number(x):
    y = random.randint(1, 100)
    if x == y:
        print("Success. Numbers matched!")
        return
    print(f"Fail. {x} and {y} does not match")


guess_number(7)
