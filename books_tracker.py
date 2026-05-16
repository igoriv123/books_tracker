import os
import json
import datetime

DATA_FILE = "books.json"

def load_books():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    else:
        return []

def save_books(books):
    with open(DATA_FILE, "w") as f:
        json.dump(books, f, indent=4, ensure_ascii=False)


def add_book(books):
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")

    while True:
        date_input = input('Введите дату прочтения книги (ГГГГ-ММ-ДД): ')
        if not date_input:
            date_added = datetime.now().strftime('%Y-%m-%d')
            print('Установленна дата по умолчанию на сегодня.')
            break

        try:
            datetime.strftime(date_input)
            date_added == date_input
            break
        except ValueError:
            print("Неправильный формат даты. Пожалуйста, используйте формат ГГГГ-ММ-ДД.")

    while True:
        try:
            raiting_input = input("Введите рейтинг книги (1-5): ")
            if 1 <= raiting_input <= 5:
                break
            else:
                print('Неправильный формат рейтинга. Пожалуйста, используйте числа от 1 до 5.')
        except ValueError:
            print("Некорректный ввод, ввдедите число от 1 до 5.")

    new_book = {
        "autor": author,
        "title": title,
        "date_added": date_added,
        "rating": raiting_input
    }

    books.append(new_book)
    save_data(books)
    print("\n Книга {title} успешно добавлена в библиотеку!")



def display_menu():
    print('=============================')
    print('1. Добавить книгу')
    print('2. Показать все книги')
    print('3. Показать среднюю оценку')
    print('4. Статистика по авторам')
    print('5. Удалить книгу')
    print('6. Выход')
    print('=============================')

def main():

    books = load_books()

    choise = input('Выберите действие (1-6): ').strip()

    if choise == '1':
        add_book()
    elif choise == '2':
        show_all_books()
    elif choise == '3':
        show_average_rating()
    elif choise == '4':
        show_author_statistics()
    elif choise == '5':
        delete_book()
    elif choise == '6':
        break
    else:
        print('Неверный выбор. Попробуйте еще раз.')


if __name__ == '__main__':
    main()

