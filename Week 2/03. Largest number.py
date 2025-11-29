# Exercise

num_one = 10
num_two = 2
num_three = 1010
num_four = 123

# Use if / else statement to find the largest number.

# Step 1: Assume the first number is the largest for now.
largest = num_one      # keep track of the current largest number

# Step 2: Compare with the second number
if num_two > largest:  # if num_two is bigger than current largest
    largest = num_two  # update largest

# Step 3: Compare with the third number
if num_three > largest:
    largest = num_three

# Step 4: Compare with the fourth number
if num_four > largest:
    largest = num_four

# Step 5: Print the final result
print("The largest number is:", largest)   # prints the biggest among all four
