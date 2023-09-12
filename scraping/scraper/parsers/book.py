"""scraper/parsers/book.py"""
import re
from scraper.locators.book_locators import BookLocators

class BookParser:
    """A class to take in an HTML page or content, and find properties of an item in it."""

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):\
        return f'<Book {self.name} {self.price}, {self.rating} stars>'

    @property
    def name(self):
        """метод select_one() знаходить лише перший тег, який відповідає селектору"""
        locator = BookLocators.NAME_LOCATOR
        # Ви можете отримати доступ до атрибутів тегу, розглядаючи тег як словник:
        item_name = self.parent.select_one(locator).attrs['title']

        return item_name
    
    @property
    def link(self):

        locator = BookLocators.LINK_LOCATOR
        item_url = self.parent.select_one(locator).attrs['href']

        return item_url
    
    @property
    def rating(self):

        locator = BookLocators.RATING_LOCATOR
        star_rating_element = self.parent.select_one(locator)
        classes = star_rating_element.attrs['class']
        rating_classes = filter(lambda x: x != 'star-rating', classes)
        rating_class = next(rating_classes)

        rating = BookParser.RATINGS.get(rating_class)

        return rating
    
    @property
    def price(self):

        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string

        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        price = float(matcher.group(1))

        return price

