from library import Library

def main() -> None:
    """Основная функция приложения."""
    library = Library('library.json')

    while True:
        print("\nМеню:\n1. Добавить книгу\n2. Удалить книгу\n3. Найти книгу\n4. Отобразить все книги\n5. Изменить статус книги\n6. Выход")
        choice = input("Выберите действие: ")
        
        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания: "))
            library.add_book(title, author, year)
        elif choice == '2':
            book_id = int(input("Введите ID книги для удаления: "))
            try:
                library.remove_book(book_id)
                print("Книга удалена.")
            except ValueError as e:
                print(e)
        elif choice == '3':
            query = input("Введите название, автора или год для поиска: ")
            results = library.search_books(query)
            if results:
                for book in results:
                    print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}")
            else:
                print("Книги не найдены.")
        elif choice == '4':
            library.display_books()
        elif choice == '5':
            book_id = int(input("Введите ID книги для изменения статуса: "))
            status = input("Введите новый статус (в наличии/выдана): ")
            try:
                library.change_status(book_id, status)
                print("Статус изменен.")
            except ValueError as e:
                print(e)
        elif choice == '6':
            break
        else:
            print("Пожалуйста, выберите корректное действие.")


if __name__ == '__main__':
    main()
