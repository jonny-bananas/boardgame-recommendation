#Below starter code copied from/based on:
#zguide Chapter 1: Basics (Ask and ye shall receive)
#URL: https://zguide.zeromq.org/docs/chapter1/
#Date: 2/5/2024

import zmq
import csv

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv().decode()
    #print(message)

    if message == "add book":
        #go into section to add a book
        #book entry in order of title, author, year, genre, rating
        new_entry = []
        socket.send_string("ready")

        title = socket.recv().decode()
        new_entry.append(title)
        socket.send_string("ready")

        author = socket.recv().decode()
        new_entry.append(author)
        socket.send_string("ready")

        year = socket.recv().decode()
        new_entry.append(year)
        socket.send_string("ready")

        genre = socket.recv().decode()
        new_entry.append(genre)
        socket.send_string("ready")

        rating = socket.recv().decode()
        new_entry.append(rating)

        with open("libraryBooks.csv", "a") as infile:
            rowwrite = csv.writer(infile)
            rowwrite.writerow(new_entry)

        socket.send_string("book added")

    elif message == "add_to_wishlist":
        socket.send_string("ready")
        book_details = socket.recv().decode().split("|")
        title, author = book_details[0], book_details[1]
        book = search_for_book(title, author)
        if book:
            copy_to_wishlist(book)
            socket.send_string("book_added_to_wishlist")
        else:
            socket.send_string("book_not_found")


    #break