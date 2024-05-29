from __init__ import CURSOR
from helpers import search_player

class player():

    def __init__(self):
        pass

    if __name__ == "__player__":
        search_or_add = input("Would you like to search for a player or add a player? ")
        if search_or_add == "search":
            search_player()
        elif search_or_add == "add":
            # add_player()
            pass
        else:
            print("Invalid choice")