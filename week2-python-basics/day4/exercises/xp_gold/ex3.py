import random


def throw_dice():
    return random.randint(1, 6)


def throw_until_doubles():
    cnt = 0
    while True:
        cnt += 1
        first = throw_dice()
        second = throw_dice()
        if first == second:
            break

    return cnt


def main():
    doubles = []
    for i in range(100):
        doubles.append(throw_until_doubles())

    print(f"Total throws: {sum(doubles)}")
    print(f"Average throws to reach doubles: {round(sum(doubles) / len(doubles), 2)}")


if __name__ == "__main__":
    main()
