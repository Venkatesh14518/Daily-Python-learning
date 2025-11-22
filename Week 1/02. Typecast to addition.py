# Type casting Exercise - 2
# Addition of string and integer using explicit conversion

# Initialise a string variable and integer variable
text_number = "10"      # string variable
count = 5               # integer variable

# After explicit conversion, use python to successfully perform
# the addition of these variables - print the result to the console
number_value = int(text_number)   # convert string to integer
total = number_value + count      # add integers
print(total)                      # prints 15

## Now try to convert this variable
total_str = str(total)            # convert integer to string
print(total_str)                  # prints "15" as string

## What kind of error does python give?
problem = total_str + count       # ❌ TypeError on this line

## What do you think the reason is?
print(problem)