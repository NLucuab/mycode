#!/usr/bin/env python3

def main():
    usr_name = input("Please enter your name:\n>")

    usr_name = usr_name.title()
    usr_date = int(
        input("Please enter your birth year in YYYY format, e.g 2010:\n>"))


    # The zodiac cycle is on a 12 year cycle, so it's safe to assume, that every 12 years, the same zodiac sign is assigned
    # I've tried out % 12 on all the years in the first if statement (2011, 1999, 1987, etc...), and they all come out to 7. 
    # I will try to use these modulo results to correspond to a key, and print out the relevant fstring value from there.

    year_modulo_12 = usr_date % 12

    zodiac_sign = {
        0: "your zodiac sign is Sheep, you are creative, resilient, gentle, mild-mannered, and shy."
    }

    print(f"{usr_name}" + zodiac_sign[year_modulo_12])


    # if usr_date in [2011, 1999, 1987, 1975, 1963]: 7 
    #     print(f"{usr_name} your zodiac sign is Rabbit, you are vigilant, witty, quick-minded, and ingenious.")
    # elif usr_date in [2020, 2008, 1996, 1984, 1972, 1960]: 4
    #     print(f"{usr_name} your zodiac sign is Rat, you are artistic, sociable, industrious, charming, and intelligent.")
    # elif usr_date in [2010, 1998, 1986, 1974, 1962]: 6
    #     print(f"{usr_name} your zodiac sign is Tiger, you are courageous, enthusiastic, confident, charismatic, and a leader.")
    # elif usr_date in [2021, 2009, 1997, 1985, 1973, 1961]: 5
    #     print(f"{user_name} your zodiac sign is Ox, you are strong, thorough, determined, loyal, and reliable.")
    # elif usr_data in [2012, 2000, 1988, 1976, 1964]: 8 
    #     print(f"{usr_name} your zodiac sign is Dragon, you are talented, powerful, lucky, and successfull.")
    # elif usr_date in [2013, 2001, 1989, 1977, 1965]: 9
    #     print(
    #         f"{usr_name} your zodiac sign is Snake, you are wise, like to work alone, and determined.")
    # elif usr_date in [2014, 2002, 1990, 1978, 1966]: 10
    #     print(
    #         f"{usr_name} your zodiac sign is Horse, you are animated, active, and energetic.")
    # elif usr_date in [2015, 2003, 1991, 1979, 1967]: 11
    #     print(f"{usr_name} your zodiac sign is Sheep, you are creative, resilient, gentle, mild-mannered, and shy.")
    # elif usr_date in [2016, 2004, 1992, 1980, 1968]:0
    #     print(
    #         f"{usr_name} your zodiac sign is Monkey, you are sharp, smart, curious, and mischievious.")
    # elif usr_date in [2017, 2005, 1993, 1981, 1969]:1
    #     print(f"{usr_name} your zodiac sign is Rooster, you are hardworking, resourceful, courageous, and talented.")
    # elif usr_date in [2018, 2006, 1994, 1982, 1970]: 2
    #     print(
    #         f"{usr_name} your zodiac sign is Dog, you are loyal, honest, cautious, and kind.")
    # elif usr_date in [2019, 2007, 1995, 1983, 1971]: 3
    #     print(f"{usr_name} your zodiac sign is Pig, you are a symbol of wealth, honesty, and practicality.")


main()
