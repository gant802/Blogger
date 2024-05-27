# lib/cli.py

from helpers import (
    exit_program,
    add_author,
    write_post
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_menu()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")

def create_menu():
    while True:
        create_menu_options()
        choice = input("> ")
        if choice == "1":
            add_author()
            main()
        elif choice == "2":
            write_post()
            main()
        elif choice == "3":
            main()
        

def create_menu_options():
    print("Please select an option:")
    print("1. Add an author")
    print("2. Write a post")
    print("3. Return to Menu")






if __name__ == "__main__":
    main()
