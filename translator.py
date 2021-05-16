MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', " ": "/", "\n": "\n"}

ENGLISH_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}


def morse_to_english(string):
    # filters the input by "\n", "\" and " "
    string = list(filter(lambda x: x != "", string.split("\n")))
    string = [list(filter(lambda x: x != "", lines.split("/"))) for lines in string]
    string = [[list(filter(lambda x: x != "", line.split(" "))) for line in lines] for lines in string]
    print(string)

    output = ""
    for line in string:
        for word in line:
            for char in word:
                if char not in ENGLISH_DICT.keys():
                    return f"Error: '{char}' is an invalid input. See the accepted keys below."
                output += ENGLISH_DICT[char]
            output += " "
        output += "\n"
    return output


def english_to_morse(string):
    output = ""
    for char in string:
        if char not in MORSE_CODE_DICT.keys():
            return f"Error: '{char}' is an invalid input. See the accepted keys below."
        elif char == " ":
            output += "/ "
        else:
            output += MORSE_CODE_DICT[char] + " "
    return output
