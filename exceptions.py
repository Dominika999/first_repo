"""
Exceptions exercise
"""

def calculate_avg(list_of_numbers):
    try:
        for val in list_of_numbers:
            if not isinstance(val, (int, float)):
                raise TypeError("Podana lista zawiera w sobie elementy nie będące liczbami!")
            
        if len(list_of_numbers) == 0:
            raise ZeroDivisionError("Podana lista jest pusta!")
            
        list_sum = 0

        for elem in list_of_numbers:
            list_sum += elem

        average = list_sum  / len(list_of_numbers)
        return average

    except TypeError as et:
        print("Error:",  et)

    except ZeroDivisionError as ez:
        print("Error:", ez)


average1 = calculate_avg([1, 2, 3, 4])
print("Średnia:", average1)
average2 = calculate_avg([])
average3 = calculate_avg([1, "abc", 2])





