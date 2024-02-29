import inquirer
import csv
import re
import socket
from pprint import pprint
from clint.textui import puts, indent, colored

BOARDGAME_LIST = 'boardgames_ranks.csv'

# removes spaces, capitals, and special characters
def normalize_text(text):
    return re.sub(r'\W+', '', text).lower()

def search_by_genre(genre):
    pass

def search_by_name(u_input, BOARDGAME_LIST):
    normy_input = normalize_text(u_input)
    with open(BOARDGAME_LIST, newline= '', encoding= 'utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if(normalize_text(row['name']) == normy_input):
                return row
    # if the name isn't on the csv then 'Nothing' is returned
    return None


def random_game():
    pass

def main():
    print("------------------------------------------------------------------------------------------")
    puts(colored.red("** Welcome! Use this program to help you find your next favorite board game!"))
    puts(colored.red("** To get started use the arrow keys to select an option below, and then hit 'enter'."))
    print("------------------------------------------------------------------------------------------\n\n")

   
    options = [
        inquirer.List(
            "options",
            message = "Choose an option:",
            choices=[
                "Search Board Game Geek's Top 50",
                "Search for a game by name",
                "Recommend a random game",
                "Quit"
            ],
        ),
    ]

    while True:
        user_choice = inquirer.prompt(options)

        # partner's microservice
        if user_choice == {'options': 'Search Board Game Geek\'s Top 50'}:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(('localhost', 32000))

            server_message = client_socket.recv(4096).decode()
            print(server_message)

            client_socket.close()

        elif user_choice == {'options': 'Search for a game by name'}:
            game_name = input("Enter the name of any Board Game: ")
            result = search_by_name(game_name, BOARDGAME_LIST)

            if result:
                print("\n")
                puts(colored.red("Is this the game you want: "))
                for key, value in result.items():
                    print(f"{key}: {value}")
                print("\n")
            else:
                puts(colored.red("Hm, that's odd. We can't find that game. Please try again.\n"))

        elif user_choice == {'options': 'Recommend a random game'}:
            random_game()

        elif user_choice == {'options': 'Quit'}:
            print("------------------------------------------------------------------------------------------")
            puts(colored.red("               Thanks for using my tool. I hope you've found it helpful!"))
            print("------------------------------------------------------------------------------------------")
            break
        else:
            print("This is an invalid option. Please try again...")
    print("\n")



if __name__ == "__main__":
    main()