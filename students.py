"""
Students data handling app
"""

name = input("Proszę podaj imię: ")
last_name = input("Proszę podaj nazwisko: ")
age = int(input("Proszę podaj wiek: "))
course = input("Proszę podaj kierunek studiów: ")
humanities_grade = float(input("Proszę podaj średnią z przedmiotow humanistycznych (od 1.0 do 6.0): "))
science_grade = float(input("Proszę podaj średnią z przedmiotow ścisłych (od 1.0 do 6.0): "))
university_name = input("Proszę podaj nazwę uniwersytetu: ")
phone_number = input("Proszę podaj numer telefonu: ")

average_grade = (humanities_grade + science_grade)/2

if not name.isalpha():
    raise ValueError("Niepoprawne dane. Błędne imię. Przerywam program.")

if not last_name.isalpha():
    raise ValueError("Niepoprawne dane. Błędne nazwisko. Przerywam program.")

if not course.isalpha():
    raise ValueError("Niepoprawne dane. Błędny kierunek studiów. Przerywam program.")

if age <= 0:
    raise ValueError("Niepoprawne dane. Wiek nie może być niższy od zera. Przerywam program.")

if humanities_grade < 1.0 or humanities_grade > 6.0:
    raise ValueError("Niepoprawne dane. Średnia z przedmiotów humanistycznych powinna być z zakresu 1.0 do 6.0. Przerywam program.")

if science_grade < 1.0 or science_grade  > 6.0:
    raise ValueError("Niepoprawne dane. Średnia z przedmiotów ścisłych powinna być z zakresu 1.0 do 6.0. Przerywam program.")

if len(phone_number) != 9 or not phone_number.isdigit():
    raise ValueError("Niepoprawne dane. Błędny numer telefonu. Przerywam program.")

print("Imię:", name)
print("Nazwisko:", last_name)
print("Wiek:", age)
print("Średnia z przedmiotów humanistycznych:", humanities_grade)
print("Średnia z przedmiotów ścisłych:", science_grade)
print("Nazwa uniwersytetu:", university_name)
print("Numer telefonu:", phone_number)
print("Średnia semestralna:", average_grade)