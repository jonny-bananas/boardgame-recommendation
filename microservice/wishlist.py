import zmq
import requests

# my temp personal API key for using Google Books so i will delete it after we present our final projects
# if you like i can show you how to generate one for yourself as well
API_KEY = "AIzaSyC9ovgCfwWQ0qsS_KQrwrjrdlBhlKA1lFc"
WISHLIST_FILE = "wishlist.txt"

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")

def search_for_book(title, author):
    query = f'intitle:"{title}"+inauthor:"{author}"'
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={API_KEY}"

    response = requests.get(url)

    if response.status_code == 200:
        book_data = response.json()
        return book_data['items'][0] if 'items' in book_data and len(book_data['items']) > 0 else None
    else:
        print("No results found. Please try the search again!")
        return None

def copy_to_wishlist(book_detail):
    with open(WISHLIST_FILE, 'a') as file:
        if book_detail:
            file.write(f"Title: {book_detail['title']}\nAuthor: {book_detail['author']}\nISBN: {book_detail['isbn']}\n\n")
        else:
            file.write("No book details available.\n")


while True:
    message = socket.recv().decode()
    if message.startswith("add_to_wishlist"):
        _, title, author = message.split("|")
        book = search_for_book(title, author)
        if book:
            book_detail = {
                'title': book['volumeInfo']['title'],
                'author': ", ".join(book['volumeInfo'].get('authors', ['No Authors'])),
                'isbn': ", ".join([identifier['identifier'] for identifier in book['volumeInfo'].get('industryIdentifiers', []) if identifier['type'] in ['ISBN_10', 'ISBN_13']])
            }
            copy_to_wishlist(book_detail)
            socket.send_string("book_added_to_wishlist")
        else:
            socket.send_string("book_not_found")