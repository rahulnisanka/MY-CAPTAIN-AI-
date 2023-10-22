def print_positive_numbers(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    print("Input: list = {}".format(numbers))
    print("Output: {}".format(positive_numbers))
    
# Input lists
list1 = [int(x) for x in input("Enter a list number separated by spaces: ").split()]
list2 = [int(x) for x in input("Enter another list of numbers separated by spaces: ").split()]

# Print positive numbers for list1
print_positive_numbers(list1)

# Print positive numebers for list2
print_positive_numbers(list2)

    