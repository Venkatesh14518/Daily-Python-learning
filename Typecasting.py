# Type Casting Exercise

a = 8

# 1. print the type of the variable
print(type(a))

#   Convert integer variable to float and confirm the type cast worked (print it out)
b=float(a)
print(type(b))


# 2. Now, Convert your float variable to string and print out the type
c=str(b)
print(type(c))


# 3. Finally, Convert your string variable back to integer and print it out (the type)
d=int(float(c))
print(type(d))