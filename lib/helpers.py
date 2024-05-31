# lib/helpers.py
from models.__init__ import CURSOR, CONN

def display_all_players():
    CURSOR.execute("SELECT * FROM players")
    players = CURSOR.fetchall()
    for player in players:
        print(f"id: {player[0]}")
        print(f"name: {player[1]}")
        print(f"PointsPerGame: {player[2]}")
        print(f"AssistsPerGame: {player[3]}")
        print(f"ReboundsPerGame: {player[4]}")
        print(f"StealsPerGame: {player[5]}")
        print(f"BlocksPerGame: {player[6]}")
        print(f"Team: {player[7]}")
        print("")
            
def display_all_teams():
    CURSOR.execute("SELECT * FROM teams")
    teams = CURSOR.fetchall()
    for team in teams:
        print(f"id: {team[0]}")
        print(f"name: {team[1]}")
        print(f"wins: {team[2]}")
        print(f"losses: {team[3]}")
        print(f"PointsPerGame: {team[4]}")
        print(f"AssistsPerGame: {team[5]}")
        print(f"ReboundsPerGame: {team[6]}")
        print(f"StealsPerGame: {team[7]}")
        print(f"BlocksPerGame: {team[8]}")
        print("")


def grab_stat_higher_than_players():
    stat = input("Enter the stat you would like to compare: ")
    value = input("Enter the value you would like to compare: ")
    CURSOR.execute(f"SELECT * FROM players WHERE {stat} > {value}")
    players = CURSOR.fetchall()
    for player in players:
        print(f"id: {player[0]}")
        print(f"name: {player[1]}")
        print(f"PointsPerGame: {player[2]}")
        print(f"AssistsPerGame: {player[3]}")
        print(f"ReboundsPerGame: {player[4]}")
        print(f"StealsPerGame: {player[5]}")
        print(f"BlocksPerGame: {player[6]}")
        print(f"Team: {player[7]}")
        print("")

def grab_stat_higher_than_teams():
    stat = input("Enter the stat you would like to compare: ")
    value = input("Enter the value you would like to compare: ")
    CURSOR.execute(f"SELECT * FROM teams WHERE {stat} > {value}")
    teams = CURSOR.fetchall()
    for team in teams:
        print(f"id: {team[0]}")
        print(f"name: {team[1]}")
        print(f"wins: {team[2]}")
        print(f"losses: {team[3]}")
        print(f"PointsPerGame: {team[4]}")
        print(f"AssistsPerGame: {team[5]}")
        print(f"ReboundsPerGame: {team[6]}")
        print(f"StealsPerGame: {team[7]}")
        print(f"BlocksPerGame: {team[8]}")
        print("")

def exit_program():
    print("Goodbye!")
    exit()
