import string
from anagram_checker import AnagramChecker


def get_user_menu_choice():
    choices = ["n", "x"]
    while choice := input("\tMenu:\n\t(n) Input a new word\n\t(x) exit\n\t: "):
        if choice in choices:
            return choice
        print("Invalid choice. Try again...")


def validate_user_input(word):
    """
    check if word only contains letters and nothing else
    return word itself it is validated otherwise - None
    """
    for c in word:
        if c.lower() not in string.ascii_lowercase:
            return
    return word


def get_user_word():
    while (user_word := validate_user_input(input("input word: ").strip())) is None:
        print(
            "You should input exactly one word, "
            "containing only alphabetic characters. Try again..."
        )
    return user_word


def print_anagrams(word, anagram_checker):
    print(
        f'Your word: "{word}"\n'
        f"This is {'valid' if anagram_checker.is_valid_word(word) else 'invalid'} English word\n"
        f"Anagrams for your word: {', '.join(anagram_checker.get_anagrams(word))}"
    )


def main():
    anagram_checker = AnagramChecker()
    while get_user_menu_choice() != "x":
        word = get_user_word()
        print_anagrams(word, anagram_checker)


if __name__ == "__main__":
    main()
