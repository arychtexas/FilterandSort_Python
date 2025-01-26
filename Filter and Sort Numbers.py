#Filter and Sort Numbers 

""" Write a program that gets a list of integers from input, and outputs non-negative integers in ascending order (lowest to highest).

Ex: If the input is:
10 -7 4 39 -6 12 2

the output is:
2 4 10 12 39 

For coding simplicity, follow every output value by a space. Do not end with newline."""

# Prompt the user to input numbers
user_input = input("Enter Numbers, e.g. 10 -7 4 39 -6 12 2: ")

# Convert the input into a list of integers
numbers = [int(num) for num in user_input.split()]

# Filter out negative numbers and sort the remaining in ascending order
positive_numbers = [num for num in numbers if num >= 0]
positive_numbers.sort()

# Print the non-negative integers with spaces, using the end argument
print(*positive_numbers, end=" ")

