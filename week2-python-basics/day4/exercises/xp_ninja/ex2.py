morse_code_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/",
}
opposite_direction = {value: key for key, value in morse_code_dict.items()}
morse_code_dict.update(opposite_direction)


def encode_to_morse(text):
    text = text.upper()  # Convert input to uppercase
    morse_text = "/".join(
        [
            " ".join(morse_code_dict[char] for char in word if char in morse_code_dict)
            for word in text.split()
        ]
    )
    morse_code = [morse_code_dict[char] for char in text if char in morse_code_dict]
    return " ".join(morse_code)


def decode_from_morse(text):
    decoded_words = []
    for word in text.split("/"):
        decoded_word = ""
        for letter in word.split():
            decoded_word += morse_code_dict[letter]
        decoded_words.append(decoded_word)
    return " ".join(decoded_words)


if __name__ == "__main__":
    encoded = encode_to_morse("Georgia is a beautiful country")
    decoded = decode_from_morse(encoded)
    print(encoded)
    print(decoded)
