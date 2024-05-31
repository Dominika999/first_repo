"""
Functions exercise
"""

test_list_1 = [1, 2, 3]
test_list_2 = [5, 312, 2, -12]
test_list_3 = [-2, -5, -2, -10]
test_list_4 = [0, 0, 0]
test_list_5 = [1, 1, 1]

list_of_tests = [test_list_1, test_list_2, test_list_3, test_list_4, test_list_5]


def sum_and_avg(my_list):
    list_sum = 0
    list_count = 0

    for elem in my_list:
        if elem % 2 == 1:
            list_sum += elem
            list_count += 1
    if list_count != 0:
        list_avg = list_sum / list_count
        print("Suma:", list_sum, "Średnia:", list_avg)
    else:
        print("W liście nie ma nieparzystych liczb!")

for test_list in list_of_tests:
    sum_and_avg(test_list)

