# Exercise

# Write a program by accepting 2 numbers from the user and check number is greater than other and print the result
# you can use the function `input()` to get user input

# example
first_number = input("please enter a number: ")       # input() ALWAYS returns a string, not a number
second_number = input("please enter another number: ")  # same here — both values are strings

print(first_number)      # prints whatever the user typed (as a string)
print(second_number)     # prints the second user input

## note, what type is your first_number? Is it what you expected?
## look-up the input() documentation to find out what type it will create by default

# Now convert the input from string → integer so we can compare numerically
first_number = int(first_number)        # int() converts the string into an integer
second_number = int(second_number)      # same conversion for second value

# Compare and print the result
if first_number > second_number:        # checks if first is greater
    print("The first number is greater")
elif first_number < second_number:      # checks if second is greater
    print("The second number is greater")
else:
    print("Both numbers are equal")     # executes if values are the same
