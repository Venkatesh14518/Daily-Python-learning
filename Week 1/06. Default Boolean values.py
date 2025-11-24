# Boolean Exercise_1
# Let's check all the default boolean values of the types we know

# make
# an int
my_int = 42                # assigning a non-zero integer; in Python any non-zero integer becomes True in boolean context

# a float
my_float = 3.14            # assigning a non-zero float; any non-zero float becomes True when converted to bool

# a string
my_string = "hello"        # assigning a non-empty string; any non-empty string becomes True when converted to bool

# the int 0
int_zero = 0               # assigning zero; the integer 0 is always False when converted to bool

# the int 1
int_one = 1                # assigning the integer 1; any non-zero integer becomes True in boolean context

# the int 1000
int_thousand = 1000        # assigning another non-zero integer; no matter how large, non-zero numbers convert to True

# now print out all the `bool()` values using the bool() function
print("bool(my_int):", bool(my_int))                   # prints True because 42 is non-zero
print("bool(my_float):", bool(my_float))               # prints True because 3.14 is non-zero
print("bool(my_string):", bool(my_string))             # prints True because "hello" is not an empty string
print("bool(int_zero):", bool(int_zero))               # prints False because 0 always converts to False
print("bool(int_one):", bool(int_one))                 # prints True because 1 is non-zero
print("bool(int_thousand):", bool(int_thousand))       # prints True because 1000 is non-zero

# are you surprised at the default boolean value for any python type?
# Key idea: in Python, bool(X) checks whether X represents "something" (True) or "nothing" (False).
# Zero → False. Empty string → False. Everything else → True.
