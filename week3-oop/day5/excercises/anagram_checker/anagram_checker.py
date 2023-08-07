import itertools
import time


class AnagramChecker:
    def __init__(self):
        # read words from file and save in set for fast checks
        with open("sowpods.txt", "r") as f:
            self.words = set([line.strip() for line in f.readlines()])

        # predefine anagram groups to easily access them when needed
        self.anagrams = {}
        for word in self.words:
            sorted_word = "".join(sorted(word))
            if sorted_word in self.anagrams:
                self.anagrams[sorted_word].append(word)
            else:
                self.anagrams[sorted_word] = [word]

    def is_valid_word(self, word):
        """check if word exists in self.words"""
        word = word.upper()
        if word in self.words:
            return True
        return False

    def get_anagrams(self, word):
        """find anagram group for given group"""
        word = word.upper()
        sorted_word = "".join(sorted(word))
        anagrams = []
        if sorted_word in self.anagrams:
            anagrams = self.anagrams[sorted_word].copy()
            if word in anagrams:
                anagrams.remove(word)
        return anagrams


if __name__ == "__main__":
    anagram_checker = AnagramChecker()
    # for word in anagram_checker.words:
    #     print(word)
    #     time.sleep(1)
    print(anagram_checker.is_valid_word("team"))
    print(anagram_checker.get_anagrams("team"))
