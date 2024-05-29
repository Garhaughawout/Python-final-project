# lib/helpers.py
from models.__init__ import CURSOR


def search_player():
    search_name = input("What player would you like to search for? ")
    CURSOR.execute(f"SELECT * FROM players WHERE name = ?", (search_name,))
    player = CURSOR.fetchone()
    print(player)
    if player:
        print(f"id: {player[0]}")
        print(f"name: {player[1]}")
        print(f"PointsPerGame: {player[2]}")
        print(f"AssistsPerGame: {player[3]}")
        print(f"ReboundsPerGame: {player[4]}")
        print(f"StealsPerGame: {player[5]}")
        print(f"BlocksPerGame: {player[6]}")
        print(f"Team: {player[7]}")
    else:
        print("Player not found")

def add_player():
    name = input("Enter the player's name: ")
    ppg = input("Enter the player's points per game: ")
    apg = input("Enter the player's assists per game: ")
    rpg = input("Enter the player's rebounds per game: ")
    spg = input("Enter the player's steals per game: ")
    bpg = input("Enter the player's blocks per game: ")
    team = input("Enter the player's team: ")

    CURSOR.execute(f"INSERT INTO players (name, PointsPerGame, AssistsPerGame, ReboundsPerGame, StealsPerGame, BlocksPerGame, Team) VALUES (?, ?)", (name, ppg, apg, rpg, spg, bpg, team))
    print("Player added successfully")


def exit_program():
    print("Goodbye!")
    exit()
