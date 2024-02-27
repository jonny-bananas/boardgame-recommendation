# osu-cs361-w24

This will be the repository that I use for CS361: Software Engineering 1 (OSU W24)

What it will eventually be is a simple command line app that will prompt the user to enter the name of a board game that they've enjoyed in the past and the app will, based off of their input, suggest them a new board game. Additional functionality will have the user to be able to search for a board game by name and be given that game's boardgamegeek.com page.

For this project I've used:
 - Miguel Ángel García's Python Inquirer: https://github.com/magmax/python-inquirer
 - Kenneth Reitz's Python CLI Tool: https://github.com/kennethreitz-archive/clint



PARTNER'S  MICROSERVICE

To demonstrate the microservice I created for my partner you have to run partners_code.py and after being presented the menu, press '4' for the option to create a wishlist and kick you over to the manage_wishlist() function in wishlist.py. At that point it will prompt you to enter the title of a book you want to add, and next it will prompt you for an author.

After entering a valid book and author it will call the Google Books API which will query the user input against Google Books' database, and if the book is found it will add the book to a .txt document titled 'wishlist.txt'. If you open the file you will find the title of the book with author and ISBN.

At that point the program kicks control back to partners_code.py and awaits for the next time its called. Eventually functionality will be managed through the use of sockets, but for now it's running from wishlist.py.

![Microservice UML Sequence Diagram](./microservice/assignment%209%20uml.png)