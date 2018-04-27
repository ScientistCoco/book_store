import unittest
from system_class import System
from stock_class import Stock
from user_class import User
from tag_class import Tag

class TestClasses(unittest.TestCase):

    def test_add_book_that_already_exists(self):
        book = System()      
        book.delete_book('112-457-128-25')
        book.add_book('Singing', '112-457-128-25', '2017-03-04', 15, 'Craig', 'Chen')
        raised = False
        try:
            book.add_book('Singing', '112-457-128-25', '2017-03-04', 15, 'Craig', 'Chen')
        except:
            raised = True
        self.assertFalse(raised)

    def test_negative_stock_change(self):
        stock = Stock()       
        with self.assertRaises(SystemExit):
            stock.increment_stock('13', -4)

    def test_add_more_than_one_tag(self):
        tag = Tag()
        raised = False
        try:
            tag.add_tag('112-457-128-25', 'Thriller')
        except:
            raised = True
        self.assertFalse(raised)
           
    def test_delete_book_not_in_system(self):
        book = System()
        raised = False
        try:
            book.delete_book('13')
        except:
            raised = True
        self.assertFalse(raised)

    def test_delete_book_in_system(self):
        book = System()
        raised = False
        try:
            book.delete_book('112-457-128-25')
        except:
            raised = True
        self.assertFalse(raised)

if __name__ == '__main__':
    unittest.main()