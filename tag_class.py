import sqlite3
import re
from database_class import Database

class Tag(object):
    # Each book is associated with a one word tag
    def __init__(self):
        self.db = Database()

    def add_tag(self, book_ISBN, tag):       
        # Adds tag to the book 
        if not (re.match("\A[\w-]+\Z", tag)):
            print("Tag can only be a single word")      
            exit()

        query = "Insert into BOOK_TAG (BOOK_ID, TAG) values ('%s', '%s')" %(book_ISBN, tag)
        try:
            self.db._dbInsert(query)
        except Exception as e:
           print(e)

    def remove_tag(self, book_ISBN):
        # Removes the tag from the book
        query = "Delete from BOOK_TAG where BOOK_ID = '%s'" %(book_ISBN)
        try:
            self.db._dbInsert(query)
        except Exception as e:
            print(e)
    
    def change_tag(self, book_ISBN, tag):
        # Changes the associated tag
        query = "Update BOOK_TAG set TAG = '%s' where BOOK_ID = '%s'" %(tag, book_ISBN)
        try:
            self.db._dbInsert(query)
        except Exception as e:
            print(e)
