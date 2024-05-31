# lib/cli.py
from models.players import Players
from models.teams import Teams
from helpers import  exit_program,  display_all_teams, display_all_players, grab_stat_higher_than_players, grab_stat_higher_than_teams

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
            print("5. Grab all teams with a stat higher than a value")
            print("6. Exit")
            new_choice = input(">")
            if new_choice == "1":
                Teams.find_by_name()
            elif new_choice == "2":
                Teams.create()
            elif new_choice == "3": 
                display_all_teams()
            elif new_choice == "4":
                Teams.grab_Players_By_Team()
            elif new_choice == "5":
                grab_stat_higher_than_teams()
            elif new_choice == "6":
                exit_program()
            else:
                print("Invalid choice")
        elif choice == "2":
            print("Please select an option:")
            print("1. Find a Player by Name")
            print("2. Create a Player")
            print("3. Display all Players")
            print("4. Grab all players with a stat higher than a value")
            print("5. Exit")
            new_choice = input(">")
            if new_choice == "1":
                Players.find_by_player_name()
            elif new_choice == "2":
                Players.create()
            elif new_choice == "3": 
                display_all_players()
            elif new_choice == "4":
                grab_stat_higher_than_players()
            elif new_choice == "5":
                exit_program()
            else:
                print("Invalid choice")
        elif choice == "3":
            player_or_team = input("Would you like to delete a player or team? ")
            if player_or_team == "player":
                Players.deletebyName()
            elif player_or_team == "team":
                Teams.deletebyName()
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
