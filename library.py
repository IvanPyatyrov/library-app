import json
import os
from typing import List, Union


class Book:
    """Класс для представления книги."""

    def __init__(self, id: int, title: str, author: str, year: int, status: str = "в наличии"):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status


class Library:
    """Класс для управления библиотекой книг."""

    def __init__(self, filename: str):
        self.filename = filename
        self.books: List[Book] = self.load_books()

    def load_books(self) -> List[Book]:
        """Загрузить книги из файла."""
        if not os.path.exists(self.filename):
            return []

        with open(self.filename, 'r') as file:
            return [Book(**book) for book in json.load(file)]

    def save_books(self) -> None:
        """Сохранить книги в файл."""
        with open(self.filename, 'w') as file:
            json.dump([vars(book) for book in self.books], file)

    def add_book(self, title: str, author: str, year: int) -> None:
        """Добавить книгу в библиотеку."""
        book_id = len(self.books) + 1
        new_book = Book(id=book_id, title=title, author=author, year=year)
        self.books.append(new_book)
        self.save_books()

    def remove_book(self, book_id: int) -> None:
        """Удалить книгу по id."""
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.save_books()
                return
        
        raise ValueError(f"Книга с ID {book_id} не найдена.")

    def search_books(self, query: Union[str, int]) -> List[Book]:
        """Искать книги по title, author или year."""
        results = []
        for book in self.books:
            if (query in book.title or 
                query in book.author or 
                (isinstance(query, int) and book.year == query)):
                results.append(book)
        return results

    def change_status(self, book_id: int, status: str) -> None:
        """Изменить статус книги по id."""
        for book in self.books:
            if book.id == book_id:
                book.status = status
                self.save_books()
                return

        raise ValueError(f"Книга с ID {book_id} не найдена.")

    def display_books(self) -> None:
        """Отобразить все книги в библиотеке."""
        for book in self.books:
            print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}")


