from datetime import datetime


def add():
    note = input("Введите заметку: ").strip()

    if note == "":
        print("Заметка не может быть пустой.")
        return

    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open("journal.txt", "a", encoding="utf-8") as f:
        f.write(date + " | " + note + "\n")

    print("Заметка сохранена.")


def list_notes():
    with open("journal.txt", "r", encoding="utf-8") as f:
        for number, line in enumerate(f, start=1):
            print(number, line.rstrip("\n"))


def search():
    text = input("Введите текст для поиска: ").strip().lower()
    found = False

    with open("journal.txt", "r", encoding="utf-8") as f:
        for number, line in enumerate(f, start=1):
            if text in line.lower():
                print(number, line.rstrip("\n"))
                found = True

    if not found:
        print("Ничего не найдено.")


while True:
    command = input("\nКоманда (add, list, search, exit): ").strip().lower()

    try:
        if command == "add":
            add()
        elif command == "list":
            list_notes()
        elif command == "search":
            search()
        elif command == "exit":
            break
        else:
            print("Неизвестная команда.")

    except FileNotFoundError:
        print("Журнал пока не создан. Добавьте первую заметку командой add.")