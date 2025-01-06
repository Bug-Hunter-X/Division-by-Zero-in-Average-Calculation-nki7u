def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    if total == 0:
        return 0 # Handle all zeros case
    average = total / len(numbers)
    return average

my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_list_with_zero = [0,0,0]
average_zero = calculate_average(my_list_with_zero)
print(f"The average of a list with zeros is: {average_zero}") #This will print 0