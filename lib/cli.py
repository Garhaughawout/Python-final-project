# lib/cli.py
from models.players import players
from models.teams import teams
from helpers import  exit_program,  display_all_teams, display_all_players

def main():
    while True:
        menu()
        choice = input(">")
        if choice == "1":
            print("Please select an option:")
            print("1. Find a Team by Name")
            print("2. Create a Team")
            print("3. Display all Teams")
            print("4. Grab all players from a team")
            new_choice = input(">")
            if new_choice == "1":
                teams.find_by_name()
            elif new_choice == "2":
                teams.create()
            elif new_choice == "3": 
                display_all_teams()
            elif new_choice == "4":
                teams.grab_Players_By_Team()
            else:
                print("Invalid choice")
        elif choice == "2":
            print("Please select an option:")
            print("1. Find a Player by Name")
            print("2. Create a Player")
            print("3. Delete a Player or Team")
            new_choice = input(">")
            if new_choice == "1":
                players.find_by_player_name()
            elif new_choice == "2":
                players.create()
            elif new_choice == "3": 
                display_all_players()
            else:
                print("Invalid choice")
        elif choice == "3":
            player_or_team = input("Would you like to delete a player or team? ")
            if player_or_team == "player":
                players.deletebyName()
            elif player_or_team == "team":
                teams.deletebyName()
            else:
                print("Invalid choice")
        elif choice == "4":
            exit_program()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("1. Work With Teams")
    print("2. Work with Players")
    print("3. Delete a Player or Team")
    print("4. Exit")


if __name__ == "__main__":
    main()
