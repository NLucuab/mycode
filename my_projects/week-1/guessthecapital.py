#!/usr/bin/python3
import os
from time import sleep

def main():
    # TODO: Refactor code to only deal with dictionary, rather than both a list & dictionary 
    # populate a countries list 
    countries = [
        "United States of America",
        "Japan",
        "South Korea",
        "Canada",
        "Egypt",
        "Finland",
        "France",
        "Greece",
        "Mexico",
        "New Zealand"
    ]

    # populate a dictionary with the countries as keys & capitals as values
    countries_and_capitals = {
        "United States of America": "Washington D.C",
        "Japan" : "Tokyo",
        "South Korea" : "Seoul", 
        "Canada" : "Ottawa",
        "Egypt" : "Cairo",
        "Finland" : "Helsinki",
        "France" : "Paris",
        "Greece" : "Athens",
        "Mexico" : "Mexico City",
        "New Zealand" : "Wellington"
    }

    print("Welcome to Guess That Capital! \n")

    print( 
    """
    Just some rules for ya:
    1) Have fun!
    2) Remember: It's just a game!
    3) Enjoy~ 
    """
    )

    username = input("May I know who's playing?: ")
    print("\n")
    print(f"Welcome, {username}! \n")


    country_count = 10
    correct_guess_count = 0
    country_idx = 0
    guess_count = 5

    while country_count > 0:

        print(f"What is the capital of {countries[country_idx]}?")

        print(f"Guesses left: {guess_count} \n")

        capital_guess = input("Enter your guess here: ").lower()

        if capital_guess == countries_and_capitals[countries[country_idx]].lower():
            print("You are correct! \n")
            correct_guess_count += 1
            country_idx += 1
            country_count -= 1
            sleep(2)
            os.system('clear')
            guess_count = 5

        elif capital_guess != countries_and_capitals[countries[country_idx]].lower() and guess_count > 1:
            print("Nice try, but not quite. Let's try one more time. \n")
            guess_count -= 1
            sleep(2)
            os.system('clear')
        
        elif capital_guess != countries_and_capitals[countries[country_idx]].lower() and guess_count == 1:
            print("Nice try, last chance! \n")
            guess_count -= 1
            sleep(2)
            os.system('clear') 
            
        elif guess_count == 0:
            print(f"Nice try! The correct answer was: {countries_and_capitals[countries[country_idx]]}. \n")
            country_idx += 1
            country_count -= 1
            sleep(2)
            os.system('clear')
            guess_count = 5
        
    print(f"You scored: {correct_guess_count}/10\n")
    print(f"Thanks for playing, {username}!")

if __name__ == "__main__":
    main()


# stretch goals:
# * get the user's name and use that throughout the game :) DONE
# * Randomize the selection of country, rather than going down the line >> opted to skip
# * Consolidate access to just the dictionary, rather than both the list & dictionary >> will come back and do this!
# * Give hints, if the user gets it wrong (set # of guesses => display that as well) >> set guess amount to 5 and displayed that!
# * print out the amount of guesses (per questions) that the user made before they got it correct DONE
# * add in invalid entry handling(entering a int, float, etc...) >>> Just made it so that it's a wrong answer!