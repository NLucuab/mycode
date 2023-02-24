#!/usr/bin/env python3

count = 0
with open("dracula.txt", "r") as dractxt:
    # another open, this time with "W" to write to vampiretimes.txt file
    with open("vampiretimes.txt", "w"):
        for line in dractxt:
            if "vampire" in line.lower():
                print(line)
print(count)