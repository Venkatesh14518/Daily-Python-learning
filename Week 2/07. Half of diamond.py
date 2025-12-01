#Exercise

#Write a Python program to construct the following pattern, using a nested for loop.
"""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

# First half of the diamond (increasing pattern)
for i in range(1, 6):              # i goes from 1 to 5 → number of stars in each row
    for j in range(i):             # print i stars
        print("*", end=" ")        # end=" " keeps stars on same line
    print()                        # print a newline after each row

# Second half of the diamond (decreasing pattern)
for i in range(4, 0, -1):          # i goes from 4 down to 1
    for j in range(i):             # print i stars
        print("*", end=" ")
    print()                        # newline after each row
