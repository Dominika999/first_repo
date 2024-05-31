"""
Employee info
"""
import sqlite3

connection = sqlite3.connect('employees.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY,
                    employee_info TEXT,
                    age INTEGER,
                    monthly_salary REAL,
                    complete_yearly_salary REAL,
                    years_of_work INTEGER,
                    position TEXT,
                    multisport INTEGER
                )''')


name = input("Proszę podaj imie: ")
last_name = input("Proszę podaj nazwisko: ")
age = int(input("Proszę podaj wiek: "))
employee_title = input("Proszę podaj tytuł naukowy: ")
monthly_salary = float(input("Proszę podaj wysokość wynagrodzenia: "))
years_of_work = float(input("Proszę podaj staż pracy: "))
position = input("Proszę podaj nazwę stanowiska: ")

multisport = False


if name == "" or last_name == "":
    raise ValueError("Brakujące dane. Przerywam program.")

if age <= 0:
    raise ValueError("Niepoprawne dane. Wiek nie może być mniejszy od zera.")

if monthly_salary < 0:
    raise ValueError("Niepoprawne dane. Wynagrodzenie miesięczne nie może być mniejsze od zera. Przerywam program.")

if years_of_work < 0:
    raise ValueError("Niepoprawne dane. Staż pracy nie może być mniejszy od zera.")

if not name.isalpha():
    raise ValueError("Niepoprawne dane. Błędne imię.")

if not last_name.isalpha():
    raise ValueError("Niepoprawne dane. Błędne imię.")

if len(position) > 12:
    raise ValueError("Niepoprawne dane. Niepoprawna nazwa stanowiska.")

employee_info = f"{name} {last_name} {employee_title}"
complete_yearly_salary = monthly_salary * 12 * 1.05
position = position.upper()

if years_of_work > 2:
    multisport = True

cursor.execute("INSERT INTO employees (employee_info, age, monthly_salary, complete_yearly_salary, years_of_work, position, multisport) \
               VALUES (?, ?, ?, ?, ?, ?, ?)", (employee_info, age, monthly_salary, complete_yearly_salary, years_of_work, position, multisport))

connection.commit()

cursor.execute("SELECT * FROM employees")
employees = cursor.fetchall()
print("Pracownicy w bazie danych:", employees)

cursor.close()
connection.close()

print("Imię:", name)
print("Nazwisko:", last_name)
print("Wiek:", age)
print("Wysokość wynagrodzenia miesięcznego:", monthly_salary)
print("Wysokość wynagrodzenia rocznego z premią:", complete_yearly_salary)
print("Staż pracy:", years_of_work)
print("Stanowisko:", position)
print("Tytuł:", employee_info)

if multisport:
    print("Pracownik posiada kartę multisport.")