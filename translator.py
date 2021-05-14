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

ENGLISH_DICT = {v:k for k,v in MORSE_CODE_DICT.items()}


class Translator:

    # morse to english translation
    def morse_to_english(self, input):

        # filters the input by "\n", "\" and " "
        input = list(filter(lambda x: x != "", input.split("\n")))
        input = [list(filter(lambda x: x != "", lines.split("/"))) for lines in input]
        input = [[list(filter(lambda x: x != "", line.split(" "))) for line in lines] for lines in input]
        print(input)

        output = ""
        for line in input:
            for word in line:
                for char in word:
                    if char not in ENGLISH_DICT.keys():
                        return f"Error: '{char}' is an invalid input. See the accepted keys below."
                    output += ENGLISH_DICT[char]
                output += " "
            output += "\n"
        return output

    # english to morse translation
    def english_to_morse(self, input):

        output = ""
        for char in input:
            if char not in MORSE_CODE_DICT.keys():
                return f"Error: '{char}' is an invalid input. See the accepted keys below."
            elif char == " ":
                output += "/ "
            else:
                output += MORSE_CODE_DICT[char] + " "
        return output
