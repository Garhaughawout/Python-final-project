# lib/cli.py

from helpers import search_player, add_player, exit_program



def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            search_player()
        elif choice == "1":
            add_player()
        elif choice == "2":
            exit_program()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Search for a player")
    print("1. Add a player")
    print("2. Exit")


if __name__ == "__main__":
    main()
