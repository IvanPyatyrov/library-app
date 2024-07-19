import unittest
import os
from library import Book, Library


class TestLibrary(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.library_filename = 'test_library.json'
        cls.library = Library(cls.library_filename)

    def setUp(self):
        """Очистка данных перед каждым тестом."""
        if os.path.exists(self.library_filename):
            os.remove(self.library_filename)

    def test_add_book(self):
        self.library.add_book("1984", "George Orwell", 1949)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "1984")
        self.assertEqual(self.library.books[0].author, "George Orwell")
        self.assertEqual(self.library.books[0].year, 1949)

    def test_remove_book(self):
        self.library.add_book("Brave New World", "Aldous Huxley", 1932)
        self.library.remove_book(1)
        self.assertEqual(len(self.library.books), 0)

    def test_search_books(self):
        self.library.add_book("Fahrenheit 451", "Ray Bradbury", 1953)
        results = self.library.search_books("Fahrenheit")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Fahrenheit 451")

    def test_change_status(self):
        self.library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
        self.library.change_status(1, "выдана")
        self.assertEqual(self.library.books[0].status, "выдана")


if __name__ == '__main__':
    unittest.main()
