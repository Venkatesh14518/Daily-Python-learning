# Exercise

# Write an explicit infinite loop
# inside the infinite loop, read integer from user as an option

# If the option is 1: print here is your first step
# If the option is 2: print "you have some steps to go"
# If the option is 3: print "you are almost done"
# If the option is 4: quit from the loop

# If the option is other number: print it is an  invalid option

while True:                          # creates an explicit infinite loop
    option = int(input("Enter an option (1–4): "))   # reads user input as an integer

    if option == 1:                  
        print("here is your first step")             # handles option 1
    elif option == 2:
        print("you have some steps to go")           # handles option 2
    elif option == 3:
        print("you are almost done")                 # handles option 3
    elif option == 4:
        break                                        # breaks the infinite loop
    else:
        print("invalid option")                      # handles any other number
