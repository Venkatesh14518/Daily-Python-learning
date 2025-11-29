#Exercise

#Write a python program in which read an integer number less than 7 from user

#If the input number is greater than or equal to 7, then print error message

#If the input is 0 print "Sunday"
#If the input is 1 print "Monday"
#If the input is 2 print "Tuesday"
#If the input is 3 print "Wednesday"
#If the input is 4 print "Thursday"
#If the input is 5 print "Friday"
#If the input is 6 print "Saturday"

#Use if-else statements

day_number = input("Enter a number between 0 and 6: ")  # input is always a string
day_number = int(day_number)                            # convert to integer so we can compare

# First check if the number is valid
if day_number >= 7 or day_number < 0:                   # if number is not in the correct range
    print("Error: number must be between 0 and 6")      # show error message

# If valid, check each case using if/elif
elif day_number == 0:
    print("Sunday")
elif day_number == 1:
    print("Monday")
elif day_number == 2:
    print("Tuesday")
elif day_number == 3:
    print("Wednesday")
elif day_number == 4:
    print("Thursday")
elif day_number == 5:
    print("Friday")
elif day_number == 6:
    print("Saturday")
