
import random

try:
    import pyperclip  #  check for util that copies text to clipboard.
except ImportError:
    pass


def main():
    print("***** L3375P34]k 63n3r470R *****")
    print("Enter your message:")
    english = input("> ")
    print()
    leetspeak = english_to_leetspeak(english)
    print(leetspeak)

    try:
        pyperclip.copy(leetspeak)
        print("(Copied leetspeak to clipboard.)")
    except NameError:
        pass


def english_to_leetspeak(message):
    """Convert english string to leetspeak"""
    char_map = {
        "a": ["4", "@", "/-\\", "^"],
        "b": ["I3", "8", "13", "|3"],
        "c": ["[", "{", "<", "("],
        "d": [")", "|)", "[)", "|>"],
        "e": ["3", "[-"],
        "f": ["|=", "ph", "|#", "/="],
        "g": ["&", "6", "(_+]", "9", "C-", "gee"],
        "h": ["#", "/-/", "[-]", "]-[", ")-(", "(-)", ":-:", "|-|", "}{"],
        "i": ["1", "[]", "!", "|", "eye", "3y3", "]["],
        "j": [",_|", "_|", "._|", "._]", ",_]", "]"],
        "k": [">|", "|<", "/<", "1<", "|c", "|(", "|{"],
        "l": ["1", "7", "|_", "|"],
        "m": ["/\\/\\", "/V\\", "JVI", "[V]", "[]V[]", "|\\/|", "^^"],
        "n": ["^/", "|\\|", "/\\/", "[\]", "<\\>", "{\\}", "|V", "/V"],
        "o": ["0", "Q", "()", "oh", "[]"],
        "p": ["|*", "|o", "?", "|^", "[]D"],
        "q": ["(_,)", "()_", "2", "O_"],
        "r": ["12", "|`", "|~", "|?", "/2", "|^", "Iz", "|9"],
        "s": ["$", "5", "z", "ehs", "es"],
        "t": ["7", "+", "-|-", "']['", '"|"', "~|~"],
        "u": ["|_|", "(_)", "V", "L|"],
        "v": ["\\/", "|/", "\\|"],
        "w": ["\\/\\/", "VV", "\\N", "'//", "\\\\'", "\\^/", "\\X/"],
        "x": ["><", ">|<", "}{", "ecks"],
        "y": ["j", "`/", "\\|/", "\\//"],
        "z": ["2", "7_", "-/_", "%", ">_", "~/_", "-\_", "-|_"],
    }
    leetspeak = ""
    for char in message:
        if char.lower() in char_map and random.random() <= 0.70:  # 70% convert
            possible_replacements = char_map[char.lower()]
            leet_replacement = random.choice(possible_replacements)
            leetspeak = leetspeak + leet_replacement
        else:
            leetspeak = leetspeak + char
    return leetspeak


if __name__ == "__main__":
    main()
