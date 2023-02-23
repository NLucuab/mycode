#!/usr/bin/python3

def guess_the_captial():
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

    """
    have a while loop that will keep going until a counter (equal to the len(countries))
    reaches 0. 
        * inside that while loop, ask print out which country the user will be guessing the capital for
        * keep a variable, starting at 0, to be the idx 
    """

    print("Welcome to Guess That Capital!")
    count = 10

    while count > 0:
        country_idx = 0
        print(f"What is the capital of {capitals[country_idx]}?")
        print("\n")
        captial_guess = input("")
