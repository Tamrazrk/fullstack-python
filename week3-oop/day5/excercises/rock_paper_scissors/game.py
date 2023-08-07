import random


class Game:
    choices_list = ["r", "p", "s"]
    wins = {
        "r": "s",
        "s": "p",
        "p": "r",
    }

    def get_user_item(self):
        """reads user's choice and validates it"""
        while True:
            choice = input("Select (r)ock, (p)aper or (s)cissors: ")
            if choice in self.choices_list:
                return choice
            print("Invalid input. Try again...")

    def get_computer_item(self):
        """generate random choice"""
        return random.choice(self.choices_list)

    def get_game_result(self, user_item, computer_item):
        """check if user won"""
        if user_item == computer_item:
            return "draw"
        if self.wins[user_item] == computer_item:
            return "win"
        return "loss"

    def play(self):
        """play one match. display and return the result"""
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(
            f"You chose: {user_item}. "
            f"The computer chose: {computer_item}. "
            f"Result: {result}"
        )
        return result
