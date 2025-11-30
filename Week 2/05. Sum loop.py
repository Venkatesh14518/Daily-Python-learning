# Exercise

# Use a for-loop to find the sum of numbers from 1 to 100
# you will need the range() function.

total = 0                         # start with a total of 0

for number in range(1, 101):      # range(1, 101) gives numbers from 1 to 100 (101 is excluded)
    total += number               # add each number to total

print("The sum is:", total)       # final result
