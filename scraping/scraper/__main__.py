from scraper import __app_name__, USER_CHOICE

from scraper.app import App


def print_best_books(app):
    print(app.get_count())
    print(app.books())
    
    for book in app.best_books():
        print(book)

def print_cheapest_books(app):
    for book in app.cheapest_books():
        print(book)


def get_next_book(app):
    print(app.next_book())

user_choices = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': get_next_book 
}


def main():
    
    user_input = input(USER_CHOICE)
    
    book_app = App()
    
    while user_input != 'q':
        if user_input in ('b', 'c', 'n'):
            user_choices[user_input](book_app)
        else:
            print("Please choose a valid command.")
        user_input = input(USER_CHOICE)
        
if __name__ == "__main__":
    main()