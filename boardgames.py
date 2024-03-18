import inquirer
import csv
import re
import socket
import random
from pprint import pprint
from clint.textui import puts, indent, colored

BOARDGAME_LIST = 'boardgames_ranks.csv'

# removes spaces, capitals, and special characters
def normalize_text(text):
    return re.sub(r'\W+', '', text).lower()

def search_by_name(u_input, BOARDGAME_LIST):
    normy_input = normalize_text(u_input)
    with open(BOARDGAME_LIST, newline= '', encoding= 'utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if(normalize_text(row['name']) == normy_input):
                return{
                    'Name' : row['name'],
                    'Rank' : row['rank'],
                    "BGG Average" : row['average'],
                    "Year Published" : row["yearpublished"]
                }
            
    # if the name isn't on the csv then 'Nothing' is returned
    return None


def random_game():
    with open(BOARDGAME_LIST, newline='', encoding= 'utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        game_names = [row['name'] for row in reader] # stores the names of each game in a variable

        if game_names:
            return random.choice(game_names)
        else:
            return None


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
                "Feature Explanation",
                "Find a random game",
                "Search for a game by name",
                "Search BoardGameGeek's Top 50",
                "Quit"
            ],
        ),
    ]

    # Sam's socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 32000))

    while True:
        user_choice = inquirer.prompt(options)

        # partner's microservice
        if user_choice == {'options': 'Search BoardGameGeek\'s Top 50'}:
            client_socket.send("get_top_50".encode())
            server_message = client_socket.recv(4096).decode()
            puts(colored.green(server_message))

        elif user_choice == {'options': 'Search for a game by name'}:
            game_name = input("Enter the name of any Board Game: ")
            result = search_by_name(game_name, BOARDGAME_LIST)

            if result:
                print("\n")
                puts(colored.red("Is this the game you want: \n"))
                for key, value in result.items():
                    puts(colored.green(f"{key}: {value}"))
                print("\n")
            else:
                puts(colored.red("Hm, that's odd. I can't find that game. Please try again.\n"))

        elif user_choice == {'options': 'Find a random game'}:
            game = random_game()
            puts(colored.red(f"""I pulled "{game}" out of my magic hat!\n\n"""))

        elif user_choice == {'options': 'Feature Explanation'}:
            puts(colored.white("-------------------------------------------------------------------------------------------------------------------"))
            puts(colored.red("'Find a Random Game': searches Board Game Geek's game database and suggests a random game.\n"))
            puts(colored.red("'Search for a Game by Name' allows you to enter the name of a board game you're interested in.\n"))
            puts(colored.red("'Search BoardGameGeek\'s Top 50' displays that day's top 50 board games, according to the BoardGameGeek website."))
            puts(colored.white("-------------------------------------------------------------------------------------------------------------------\n\n"))

        elif user_choice == {'options': 'Quit'}:
            client_socket.send("quit".encode())
            print("------------------------------------------------------------------------------------------")
            puts(colored.red("               Thanks for using my tool. I hope you've found it helpful!"))
            print("------------------------------------------------------------------------------------------")
            client_socket.close()
            break
        else:
            print("This is an invalid option. Please try again...")
    print("\n")


if __name__ == "__main__":
    main()