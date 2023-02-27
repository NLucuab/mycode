#!/usr/bin/env python3
import os
from time import sleep

def main():
    bottle_count = int(input("How many bottles of beer on the wall should there be?: "))

    while int(bottle_count) >= 100:
        bottle_count = input("That's simply too many bottles! Let's choose something under 100, shall we?: ")

    print("Thank you for that!")

    bottle_count = int(bottle_count)

    sleep(2)
    os.system("clear")
    
    for num in range(bottle_count, 0, -1):
        print(f"{num} bottles of beer on on the wall! \n")
        print(f"{num} bottles of beer on the wall! {num} bottles of beer! You take one down, pass it around!\n")



if __name__ == '__main__':
    main()