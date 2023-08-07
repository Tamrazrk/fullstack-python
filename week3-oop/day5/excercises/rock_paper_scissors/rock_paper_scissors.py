from game import Game


def get_user_menu_choice():
    choices = ["g", "x"]
    choice = input("\tMenu:\n\t(g) Play a new game\n\t(x) Show scores and exit\n\t: ")
    if choice in choices:
        return choice


def print_results(results):
    print(
        f"\tGame Results:\n"
        f"\t You won {results['win']} times\n"
        f"\t You lost {results['loss']} times\n"
        f"\t You drew {results['draw']} times\n\n"
        f"\tThank you for playing!"
    )


def main():
    results = {
        "win": 0,
        "loss": 0,
        "draw": 0,
    }
    while user_choice := get_user_menu_choice() != "x":
        game = Game()
        result = game.play()
        results[result] += 1

    print_results(results)


if __name__ == "__main__":
    main()
