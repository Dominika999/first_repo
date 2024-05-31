"""
TO:DO app
"""
todo_list = []
   
print("TO:DO app")
while True:
    print("'''''''''")
    print("Dostępne opcje:")
    print("1. Wyświetl listę")
    print("2. Dodaj nowe zadanie")
    print("3. Wyczyść listę")
    print("4. Wyjdź z programu")
    print("'''''''''")
    option = input("Proszę wybierz opcję (1-5): ")
    if option == '1':
        if not todo_list:
            print("Lista zadań jest pusta.")
        else:
            print("Lista zadań:")
            print(todo_list)
    elif option == '2':
        task = input("Wpisz zadanie do dodania: ")
        todo_list.append(task)
        print("Zadanie zostało dodane do listy.")  
    elif option == '3':
        todo_list.clear()
        print("Lista została wyczyszczona.")
    elif option == '4':
        print("Wychodzę z programu!")
        break
    else:
        print("Nie istnieja taka opcja. Proszę wybierz opcję (1-5): ")
