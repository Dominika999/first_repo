"""
TO:DO app
"""

todo_list = []

print("TO:DO app")

while True:
    print("''''''")
    print("Dostępne opcje:")
    print("1. Wyświetl listę")
    print("2. Dodaj nowe zadanie")
    print("3. Zaznacz zadanie jako wykonane")
    print("4. Wyczyść listę")
    print("5. Usuń wybrane zadanie")
    print("6. Wyjdź z aplikacji")
    print("''''''")

    option = int(input("Proszę wybierz opcję (1-4): "))

    if option == 1:
        if not todo_list:
            print("Lista zadań jest pusta.")
        else:
            print("Lista zadań:")
            for number, task in enumerate(todo_list, 1):
                print(f"{number}. {task}")
    elif option == 2:
        task = input("Wpisz zadanie do dodania: ")
        todo_list.append(task)
        print("Zadanie zostało dodane do listy.")
    elif option == 3:
        if not todo_list:
            print("Lista zadań jest pusta.")
        else:
            for number, task in enumerate(todo_list, 1):
                print(f"{number}. {task}")
            while True:
                task_number = int(input("Podaj numer zadania do oznaczenia jako wykonane: "))
                if 1 <= task_number <= len(todo_list):
                    todo_list[task_number - 1] += " (Wykonane)"
                    print("Zadanie zostało oznaczone jako wykonane.")
                    break
                else:
                    print("Podano nieprawidłowy numer zadania.")
    elif option == 4:
        todo_list.clear()
        print("Lista została wyczyszczona.")
    elif option == 5:
        if not todo_list:
            print("Lista zadań jest pusta.")
        else:
            print("Lista zadań:")
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")
            while True:
                task_number = int(input("Podaj numer zadania do usunięcia: "))
                if 1 <= task_number <= len(todo_list):
                    del todo_list[task_number - 1]
                    print("Zadanie zostało usunięte.")
                    break
                else:
                    print("Podano nieprawidłowy numer zadania.")
    elif option == 6:
        print("Koniec programu")
        break
    else:
        print("Nie istnieje taka opcja.")





