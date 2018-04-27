import sqlite3

class Database(object):
    
    def __init__(self):
        pass

    def _dbInsert(self, query):
        connection = sqlite3.connect('bookshop.db')
        connection.execute("PRAGMA foreign_keys = 1")
        cursorObj = connection.cursor()

        # Executes the query
        cursorObj.execute(query)
        connection.commit()
        cursorObj.close()

    def _dbSelect(self, query):
        connection = sqlite3.connect('bookshop.db')
        cursorObj = connection.cursor()

        #Executes the query
        rows = cursorObj.execute(query)
        connection.commit()
        results = ()
        for row in rows:
            results = results + row
        cursorObj.close()
        return results     