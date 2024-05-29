# lib/cli.py
from helpers import search_player, add_player, exit_program, search_team, add_team

def main():
    while True:
        menu()
        choice = input(">")
        if choice == "0":
            search_player()
        elif choice == "1":
            search_team()
        elif choice == "2":
            add_team()
        elif choice == "3":
            add_player()
        elif choice == "4":
            exit_program()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Search for a player")
    print("1. Search a team")
    print("2. Add a team")
    print("3. Add a player")
    print("4. Exit")


if __name__ == "__main__":
    main()
