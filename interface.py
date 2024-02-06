import inquirer
from pprint import pprint
from clint.textui import puts, indent, colored


def recommend_similar(game_name):
    pass

def search_by_name(game_name):
    pass

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
                "Recommend a similar game",
                "Search for a game by name",
                "Recommend a random game",
                "Quit"
            ],
        ),
    ]

    while True:
        user_choice = inquirer.prompt(options)

        if user_choice == {'options': 'Recommend a similar game'}:
            game_name = input("Enter the name of a game you enjoy: ")
            recommend_similar(game_name)
            break

        elif user_choice == {'options': 'Search for a game by name'}:
            game_name = input("Enter the name of any Board Game: ")
            search_by_name(game_name)
            break

        elif user_choice == {'options': 'Recommend a random game'}:
            break

        elif user_choice == {'options': 'Quit'}:
            break

        else:
            print("This is an invalid option. Please try again...")

    print("\n\n")



if __name__ == "__main__":
    main()