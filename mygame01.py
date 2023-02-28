#!/usr/bin/python3

def showInstructions():
    print("""
    RPG Game
    ========
    Commands:
        go [direction]
        get [item]
    """)

    def showStatus():
        # determine the current status of the player
        print("---------------------------")
        print("You are in the " + currentRoom)

        print("Inventory:" + inventory)

        if "item" in rooms[currentRoom]:
            print("You see a " + rooms[currentRoom]["item"])
        print("---------------------------")

inventory = []

rooms = {

}