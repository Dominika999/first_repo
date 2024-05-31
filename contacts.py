"""
Phone book app
"""

contacts = {}

print("""
Twoje kontakty:
1 - Dodaj nowy kontakt
2 - Usuń kontakt
3 - Wyszukaj kontakt
4 - Zmodyfikuj numer kontaktu
5 - Wyświetl kontakty
6 - Wyjdź z zakładki kontakty
""")


def validate_and_save_number(name, message):
    phone = input("Proszę podaj nowy numer telefonu: ")
    phone = phone.replace(" ", "")
    if phone.isdigit() and len(phone) == 9:
        contacts[name] = phone
        print(f"Numer został {message}.")
    else:
        print("Podano nieprawidłowy numer telefonu.")


def add_new_contact():
    name = input("Proszę podaj nazwę kontaktu do dodania: ")
    if name in contacts:
        print("Podany kontakt już istnieje!")
    else:
        validate_and_save_number(name, "dodany")


def delete_contact():
    name = input("Proszę podaj nazwę kontaktu do usunięcia: ")
    if name in contacts:
        del contacts[name]
        print("Kontakt został usunięty.")
    else:
        print("Podany kontakt nie istnieje.")


def search_contact():
    name = input("Proszę podaj nazwę kontaktu do wyszukania: ")
    if name in contacts:
        print("Numer telefonu:", contacts[name])
    else:
        print("Podany kontakt nie istnieje.")


def modify_contact():
    name = input("Proszę podaj nazwę kontaktu do modyfikacji: ")
    if name in contacts:
        validate_and_save_number(name, "zmodyfikowany")
    else:
        print("Podany kontakt nie istnieje!")


def show_contacts():
    if len(contacts) == 0:
        print("Brak zapisanych kontaktów.")
    else:
        for key, val in contacts.items():
            print(key, val)


while True:
    option = int(input("Proszę wybierz opcję (1-6): "))

    if option == 1:
        add_new_contact()
    elif option == 2:
        delete_contact()
    elif option == 3:
        search_contact()
    elif option == 4:
        modify_contact()
    elif option == 5:
        show_contacts()
    elif option == 6:
        print("Wychodzę z zakładki kontakty.")
        break
    else:
        print("Opcja poza zakresem dozwolonych!")
