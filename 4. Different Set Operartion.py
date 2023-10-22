# Define two sets
E = set(input("Enter the elements of set E separated by commas: ").split(','))
N = set(input("Enter the elements of set N separated by commas: ").split(','))

# Perform set operations
union_result = E | N # Union
intersection_result = E & N # Intersection
difference_result = E - N # Difference
symmetric_difference_result = E ^ N # Symmetric Difference

# Print the results
print("Union of E and N is", union_result)
print("Intersection of E and N is", intersection_result)
print("Difference of E and N is", difference_result)
print("Symmetric difference of E and N is", symmetric_difference_result)