import requests

from scraper import URL
from scraper.pages import Pages

class App:
    _books = []
    
    def __init__(self) -> None:
        self.page_content = requests.get(URL).content
        self.page = Pages(self.page_content)
        
        self._books = self.books()
        self.books_generator = (x for x in self._books)
        
    def get_count(self):
        return self.page.page_count
        
    def books(self):
       books = []
       for page_num in range(self.page.page_count):
          
           url = f'{URL}/catalogue/page-{page_num+1}.html'
           page_content = requests.get(url).content
           page = Pages(page_content)
           books.extend(page.books)
      
       return books
   
    def next_book(self):
       return next(self.books_generator)

    def best_books(self):
       best_books = sorted(self._books, key=lambda x: x.rating * -1)[:5]
       return best_books

    def cheapest_books(self):
       cheapest_books = sorted(self._books, key=lambda x: x.price)[:5]
       return cheapest_books
  
