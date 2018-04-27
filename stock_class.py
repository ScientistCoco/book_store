import sqlite3
from database_class import Database

class Stock(object):
    
    def __init__(self):
        self.db = Database()

    def increment_stock(self, book_ISBN, increment_amount):
        # Increment the stock in the stock table by the increment_amount
        # Check that the number the user entered > 0 
        if (increment_amount < 0):
            print("Please put in a value that is greater than 0")
            exit()

        query = "Update STOCK_LEVEL set AMOUNT = AMOUNT + %d where BOOK_ID = '%s'" %(increment_amount, book_ISBN)

        try:
            self.db._dbInsert(query)
        except Exception as e:
            print(e)

    def decrement_stock(self, book_ISBN, decrement_amount):
        # Decrement the stock in the stock table by the decrement_amoumt
        # Check that the number the user entered > 0
        if (decrement_amount < 0):
            print("Please put in a value that is greater than 0")
            exit()

        query = "Update STOCK_LEVEL set AMOUNT = AMOUNT - %d where BOOK_ID = '%s'" %(decrement_amount, book_ISBN)

        try:
            self.db._dbInsert(query)
        except Exception as e:
            print(e)