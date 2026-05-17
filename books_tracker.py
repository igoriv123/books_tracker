import os
import json
from datetime import datetime

DATA_FILE = "books.json"

def load_books():

    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Ошибка чтения файла данных. Начинаем с пустым списком книг.")
        return []
    except Exception as e:
        print(f"Произошла ошибка при загрузке данных: {e}")
        return []

def save_books(books):
    try:
        with open(DATA_FILE, "w", encoding='utf-8') as f:
            json.dump(books, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Ошибка при сохранении данных: {e}")



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
            datetime.strptime(date_input, "%Y-%m-%d")
            date_added = date_input
            break
        except ValueError:
            print("Неправильный формат даты. Пожалуйста, используйте формат ГГГГ-ММ-ДД.")

    while True:
        try:
            raiting_input = int(input("Введите рейтинг книги (1-5): ").strip())
            if 1 <= raiting_input <= 5:
                break
            else:
                print('Неправильный формат рейтинга. Пожалуйста, используйте числа от 1 до 5.')
        except ValueError:
            print("Некорректный ввод, ввдедите число от 1 до 5.")

    new_book = {
        "author": author,
        "title": title,
        "date_added": date_added,
        "rating": raiting_input
    }

    books.append(new_book)
    save_books(books)
    print("\n Книга {title} успешно добавлена в библиотеку!")

def show_all_books(books):
    if not books:
        print("\n Пока нет ни одной прочитанной книги.")
        return

    print("\n--- Список всех прочитанных книг ---")
    print(f"{'Название':<30} | {'Автор':<20} | {'Оценка':<6} | {'Дата':<12}")
    print("-" * 75)
    for book in books:
        print(f"{book['title'][:29]:<30} | {book['author'][:29]:<30} | {book['rating']:<6} | {book['date_added']:<12}")
    print("-" * 75)

def show_average_rating(books):
    if not books:
        print("\n Для расчета средней оценки нужно добавить книги.")
        return

    total_rating = sum(book['rating'] for book in books)
    average = total_rating / len(books)
    print(f"\n Общая средняя оценка всех книг: {average:.2f} из 5.0")

def show_author_statistics(books):
    if not books:
        print("\n Нет данных для анализа авторов.")
        return

    author_ratings = {}
    author_counts = {}

    for book in books:
        author = book['author'].lower()
        rating = book['rating']
        
        if author not in author_ratings:
            author_ratings[author] = 0
            author_counts[author] = 0
        
        author_ratings[author] += rating
        author_counts[author] += 1

    print("\n Статистика по авторам:")
    print("----------------------------------------")
    for author, total_rating in author_ratings.items():
        count = author_counts[author]
        average = total_rating / count
        print(f"Автор: {author.capitalize():<15} | Книг: {count} | Средняя оценка: {average:.2f}")
    print("----------------------------------------")

def delete_book(books):
    if not books:
        print("\n Список пуст, удалять нечего.")
        return
        
    show_all_books(books)
    
    while True:
        try:
            index_to_delete = input("\n Введите номер книги, которую хотите удалить (или 'отмена'): ")
            if index_to_delete.lower() == 'отмена':
                return

            index = int(index_to_delete) - 1
            if 0 <= index < len(books):
                removed_book = books[index]
                confirm = input(f"Вы уверены, что хотите удалить '{removed_book['title']}' от {removed_book['author']}? (да/нет): ").lower()
                if confirm == 'да':
                    deleted_book = books.pop(index)
                    save_books(books)
                    print(f"\n Книга '{deleted_book['title']}' успешно удалена.")
                    return
                else:
                    print("Удаление отменено. ")
                    return
            else:
                print("Пожалуйста, введите корректный номер книги.")
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")

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

    while True:
        display_menu()
        choice = input('Выберите действие (1-6): ').strip()

        if choice == '1':
            add_book(books)
        elif choice == '2':
            show_all_books(books)
        elif choice == '3':
            show_average_rating(books)
        elif choice == '4':
            show_author_statistics(books)
        elif choice == '5':
            delete_book(books)
        elif choice == '6':
            break
        else:
            print('Неверный выбор. Попробуйте еще раз.')


if __name__ == '__main__':
    main()

