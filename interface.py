import inquirer
from pprint import pprint
from clint.textui import puts, indent, colored


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
                "Search for a game by name",
                "Quit"
            ],
        ),
    ]

    user_choice = inquirer.prompt(options)
    pprint(user_choice)

# def userActions():
#     # Main Menu Options #
#     userActions = inquirer.select(
#         msg = "Select an option:",
#         choices = [
#             "Search a game by name"
#         ],
#         default = "Search a game by name",
#     ).execute()
#     return userActions




if __name__ == "__main__":
    main()