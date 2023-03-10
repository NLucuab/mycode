#!/usr/bin/env python3

def main():
    # Which character do you want to know about? (Starlord, Mystique, Hulk)
    char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk: ")

    char_stat = input("Which statistic do you want to know about? (real name, powers, archenemy: ")

    marvelchars= {
    "Starlord":
    {"real name": "peter quill",
    "powers": "dance moves",
    "archenemy": "Thanos"},

    "Mystique":
    {"real name": "raven darkholme",
     "powers": "shape shifter",
     "archenemy": "Professor X"},

    "Hulk":
    {"real name": "bruce banner",
    "powers": "super strength",
    "archenemy": "adrenaline"}
             }
    print(f"{char_name.title()}\'s {char_stat.lower()} is: {marvelchars[char_name.title()][char_stat.lower()]}.")

if __name__ == "__main__":
    main()
