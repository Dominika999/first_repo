"""
Sales calculations
"""

import csv

sales_data = open("sales_data_sample.csv", "r")

csv_sales_data = csv.reader(sales_data)

for row in range(7):
    print(next(csv_sales_data))

sales_data.seek(0)
next(sales_data)

total_revenue = 0


min_year = 1000000
max_year = 0

for row in csv_sales_data:
    total_revenue += float(row[4])

    if int(row[9]) < min_year:
        min_year = int(row[9])
    if int(row[9]) > max_year:
        max_year = int(row[9])

print("Całkowity przychod wynosi:", total_revenue)
print("Zakres lat: od", min_year, "do", max_year)

sales_result = open("sales_sum.txt", "w", encoding="utf-8")
sales_result.write(f"Całkowity przychód wynosi: {total_revenue}\n")
sales_result.write(f"Zakres lat: od {min_year} do {max_year}")

sales_data.close()
sales_result.close()







