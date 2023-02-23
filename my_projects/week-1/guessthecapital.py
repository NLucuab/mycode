#!/usr/bin/python3

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

    # have a while loop that will keep going until a counter (equal to the len(countries))
    # reaches 0. 
    #     * inside that while loop, ask print out which country the user will be guessing the capital for
    #     * keep a variable, starting at 0, to be the idx tracker for the countries list
    #     * increment the country_idx counter after every guess
    #     * keep a variable that keeps track of correct guesses
    #     * increment the correct guess counter when a guess is correct

    print("Welcome to Guess That Capital! \n")
    country_count = 10
    correct_guess_count = 0
    country_idx = 0

    while country_count > 0:
        print(f"What is the capital of {countries[country_idx]}?")
        captial_guess = input("Enter your guess here: ").lower()

        if captial_guess == countries_and_capitals[countries[country_idx]].lower():
            print("You are correct! \n")
            correct_guess_count += 1

        else:
            print("Nice try, but not quite correct there. \n")
            
        country_count -= 1
        country_idx += 1
        
    
    print("Thank you for playing the game! \n")
    print(f"You scored: {correct_guess_count}/10")

if __name__ == "__main__":
    main()


# stretch goals:
# * get the user's name and use that throughout the game :) 
# * Randomize the selection of country, rather than going down the line
# * Consolidate access to just the dictionary, rather than both the list & dictionary
# * Give hints, if the user gets it wrong (set # of guesses => display that as well)
# * print out the amount of guesses (per questions) that the user made before they got it correct
# * add in invalid entry handling(entering a int, float, etc...)