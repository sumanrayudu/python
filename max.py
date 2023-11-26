#Author: Suman
#Date

# List of numbers
numbers = [5, 8, 2, 10, 3]

# Initialize a variable to store the maximum value
maximum = numbers[0]

# Iterate through the list
for num in numbers:
    if num > maximum:
        maximum = num

# Print the maximum value
print("Maximum value:", maximum)