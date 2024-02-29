import requests

# my temp personal API key for using Google Books so i will delete it after we present our final projects
# if you like i can show you how to generate one for yourself as well
API_KEY = "AIzaSyC9ovgCfwWQ0qsS_KQrwrjrdlBhlKA1lFc"
WISHLIST_FILE = "wishlist.txt"

def manage_wishlist():
    print("\n\n")
    print("---------------------------------------------------------------------------------------------")
    print("                     You've chosen to add a book to your wishlist!")
    print("** In order for this to work you'll have to enter BOTH the title of the book and the author **")
    print("---------------------------------------------------------------------------------------------\n\n")
    
    title = input("What is the name of the book you want to add?: ")
    author = input(f"Who is the author of {title}?: ")

    # saves the returned result as 'book'
    book = search_for_book(title, author)

    # parsing explanations are also here: https://developers.google.com/books/docs/v1/using
    if book:
        book_detail = {
            'title': book['volumeInfo']['title'],
            'author': ", ".join(book['volumeInfo'].get('authors', ['No Authors'])),
            'isbn': ", ".join([identifier['identifier'] for identifier in book['volumeInfo'].get('industryIdentifiers', []) if identifier['type'] in ['ISBN_10', 'ISBN_13']])
        }    
        copy_to_wishlist(book_detail)
        print(f"\nI've added {title} to {WISHLIST_FILE}\n\n")
        return
    else:
        print(f"\nSorry I couldn't find the book {title} by {author}.\n\n")
        return

def search_for_book(title, author):
    # this is the formula for using Google Books' API
    # https://developers.google.com/books/docs/v1/using - documentation
    query = f'intitle:"{title}"+inauthor:"{author}"'
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={API_KEY}"

    response = requests.get(url)

    # grabs only the first result from the json that the api returns
    if response.status_code == 200:
        book_data = response.json()
        return book_data['items'][0] if 'items' in book_data and len(book_data['items']) > 0 else None
    else:
        print("No results found. Please try the search again!")
        return None
    
def copy_to_wishlist(book_detail):
    # opens the .txt file in append mode and adds each book to the end of the list
    with open(WISHLIST_FILE, 'a') as file:
        if book_detail:
            file.write(f"Title: {book_detail['title']}\nAuthor: {book_detail['author']}\nISBN: {book_detail['isbn']}\n\n")
        else:
            file.write("No book details available.\n")


''' # some things to note
    # if you type in the partial name of a series of boos like 'harry potter' for example, it will always return the first book. 
        #'harry potter and the philosopher's stone' in this example

    # you can use all upper-case, lower-case, or camel case and it should still work
        
    # i currently have it breaking the loop but if you want it to loop back to the main menu you can just remove the 'break' statements '''
    