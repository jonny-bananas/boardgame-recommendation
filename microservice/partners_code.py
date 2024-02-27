#Below starter code copied from/based on:
#zguide Chapter 1: Basics (Ask and ye shall receive)
#URL: https://zguide.zeromq.org/docs/chapter1/
#Date: 2/5/2024

import zmq
import pandas
import wishlist
from wishlist import manage_wishlist

context = zmq.Context()
#  Socket to talk to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555") #this will connect to libraryServer

print(f"Hello! Welcome to your personal library/catalog! \n With this catalog, you can add books that you own to a "
      f"virtual library to help you keep track of them.  You can also view all of the books in your library. \n\n"
      f"New features will be described as they are implemented \n\n"
      f"To interact with your library, select from one of the options below!\n\n"
      f"   Enter 1 or add to add a book to your catalog\n"
      f"   Enter 2 or view to view the books in your catalog\n"
      f"   Enter 3 or exit to quit the program\n"
      f"   Enter 4 or wishlist to add a book to your wishlist\n\n")


while True:

    user_input = input("Enter option for interacting with your library: ")

    if user_input == "1" or user_input.lower() == "add":
        # book entry in order of title, author, year, genre, rating
        socket.send_string(f"add book")
        rec_mes = socket.recv().decode()
        if rec_mes == "ready":
            print(f"You have chosen to add a new book to your library. Enter the info from the prompts that"
                           f"appear below. \n **The only required fields are the title and author, if you "
                           f"wish to leave a field blank, hit enter** \n\n")

        title = input("Enter title: ")
        while title == "":
            print("Title is required, please enter an input\n")
            title = input("Enter title: ")
        print(f"This is the title you entered: {title}")
        checks = input("If this is correct, type 'y' otherwise type 'n' to re-enter it: ")
        if checks.lower() == 'n' or checks.lower() == "no":
            title = input("Enter title: ")
        socket.send_string(f"{title}")

        rec_mes = socket.recv().decode()
        if rec_mes != "ready":
            print("There was an error, exiting the program")
            break

        author = input("Enter Author: ")
        while author == "":
            print("Author is required, please enter an input\n")
            author = input("Enter author: ")
        print(f"This is the author you entered: {author}")
        checks = input("If this is correct, type 'y' otherwise type 'n' to re-enter it: ")
        if checks.lower() == 'n' or checks.lower() == "no":
            author = input("Enter author: ")
        socket.send_string(f"{author}")

        rec_mes = socket.recv().decode()
        if rec_mes != "ready":
            print("There was an error, exiting the program")
            break

        year = input("Enter Year Released: ")
        if year == "":
            year = "none"
            socket.send_string(f"{year}")
        else:
            print(f"This is the year you entered: {year}")
            checks = input("If this is correct, type 'y' otherwise type 'n' to re-enter it: ")
            if checks.lower() == 'n' or checks.lower() == "no":
                year = input("Enter year: ")
            socket.send_string(f"{year}")

        rec_mes = socket.recv().decode()
        if rec_mes != "ready":
            print("There was an error, exiting the program")
            break

        genre = input("Enter Genre: ")
        if genre == "":
            genre = "none"
            socket.send_string(f"{genre}")
        else:
            print(f"This is the genre you entered: {genre}")
            checks = input("If this is correct, type 'y' otherwise type 'n' to re-enter it: ")
            if checks.lower() == 'n' or checks.lower() == "no":
                genre = input("Enter genre: ")
            socket.send_string(f"{genre}")

        rec_mes = socket.recv().decode()
        if rec_mes != "ready":
            print("There was an error, exiting the program")
            break

        rating = input("Enter Rating out of 5 stars: ")
        if rating == "":
            rating = "none"
            socket.send_string(f"{rating}")
        else:
            print(f"This is the rating you entered: {rating}")
            checks = input("If this is correct, type 'y' otherwise type 'n' to re-enter it: ")
            if checks.lower() == 'n' or checks.lower() == "no":
                title = input("Enter rating: ")
            socket.send_string(f"{rating}")

        rec_mes = socket.recv().decode()
        if rec_mes == "book added":
            print(f"Your book has been successfully added to your catalog!\n\n")


    elif user_input == "2" or user_input.lower() == "view":
        books = pandas.read_csv('libraryBooks.csv')
        print(books)


    elif user_input == "3" or user_input.lower() == "exit":
        print("You've opted to quit the program, have a nice day!")
        socket.send_string(f"close_program")
        break


    elif user_input == "4" or user_input.lower() == "wishlist":
        manage_wishlist()


    else:
        print("Your input was not recognized, please enter another input")