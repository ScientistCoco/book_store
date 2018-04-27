import sqlite3
from database_class import Database

class System(object):

    def __init__(self):
        self.db = Database()

    def add_book(self, book_name, book_ISBN, publication_date, price, author_firstname, author_lastname):
        # Add the book to the database
        try:
            query1 = "Insert into BOOK values ('%s', '%s', '%s', %11.2f)" %(book_ISBN, book_name, publication_date, price)
            query2 = ("Insert into AUTHOR (GIVEN_NAME, LAST_NAME, BOOK_ID) values ('%s', '%s', '%s')" 
                %(author_firstname, author_lastname, book_ISBN))
            self.db._dbInsert(query1)
            self.db._dbInsert(query2)
        except Exception as e:
            print(e)

    def delete_book(self, book_ISBN):
        # Remove the book from the database
        query = "Delete from BOOK where ISBN = '%s'" %(book_ISBN)
        try:
            self.db._dbInsert(query)
        except Exception as e:
            print(e)
