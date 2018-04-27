import sqlite3
from database_class import Database

class User(object):
    # User can search up book according to:
    # • Book name
    # • Book tags
    # • Book publication date
    # • Author's first name
    # • Author's last name
    # • Book price
    # • Or just return all the books
    # Returns the items in the format:
    # book name | author first_name + last_name | ISBN | stock level | D.O.P | price

    def __init__(self):
        self.db = Database()

    def get_all_books(self):
        # Return a list of everything in system,
        query = "select ISBN from BOOK"
        self._print_items(query)

    def get_books_by_tag(self, tag):
        # Assuming that the user can only put one tag to search, this searches the book_tag table
        query = "select BOOK_ID from BOOK_TAG where TAG = '%s'" %(tag)
        self._print_items(query)

    def get_book_by_bookname(self, bookname):
        # Returns books that match the title
        query = "select ISBN from BOOK where BOOK_NAME like '%s'" %('%' + bookname + '%')
        self._print_items(query)

    def get_books_by_date(self, date):
        # Date formatted as YYYY-MM-DD
        query = "select ISBN from BOOK where DATE_OF_PUBLICATION = '%s'" %(date)
        self._print_items(query)

    def get_books_by_firstname(self, author_firstname):
        # Returns books with the authors first name
        query = "select BOOK_ID from Author where GIVEN_NAME = '%s'" %(author_firstname)
        self._print_items(query)

    def get_books_by_lastname(self, author_lastname):
        # Returns books with the authors last name
        query = "select BOOK_ID from Author where LAST_NAME = '%s'" %(author_lastname)
        self._print_items(query)

    def get_books_by_price(self, price):
        # Check user has entered a integer not a string
        query = "select ISBN from BOOK where price = '%d'" %(price)
        self._print_items(query)    

    def _print_items(self, query):
        book_id = self.db._dbSelect(query)
        book_id = list(book_id)
        print("%-50s | %-20s | %-20s | %-18s | %-20s | %-10s" %('BOOK NAME', 'AUTHOR', 'ISBN', 'STOCK', 'DATE OF PUBLICATION', 'PRICE'))
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
        for i in range(0, len(book_id)):
            self._get_book_by_ISBN(book_id[i])
        print("\n")

    def _get_book_by_ISBN(self, ISBN):
        book_query = "Select BOOK_NAME, ISBN, PRICE, DATE_OF_PUBLICATION from BOOK where ISBN = '%s'" %(ISBN)
        author_query = "Select GIVEN_NAME, LAST_NAME from AUTHOR where BOOK_ID = '%s'" %(ISBN)
        stock_query = "Select AMOUNT from STOCK_LEVEL where BOOK_ID = '%s'" %(ISBN)  
        try:
            book_tuple = self.db._dbSelect(book_query)
            author_tuple = self.db._dbSelect(author_query)
            stock_tuple = self.db._dbSelect(stock_query)

            print("%-50s | %-20s | %-20s | %-18d | %-20s | %-10d" %(book_tuple[0], author_tuple[0] + ' ' + author_tuple[1], 
                book_tuple[1], stock_tuple[0], book_tuple[3], book_tuple[2]))           
        except Exception as e:
            print(e)