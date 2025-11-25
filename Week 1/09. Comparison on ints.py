# Run some basic comparisons on basic integers and floating points

# what is bigger, a or b?
a = 2              # assigns the integer value 2 to variable a
b = 10             # assigns the integer value 10 to variable b

print("a:", a, "b:", b)        # prints both values, helpful to see the numbers
print("Is a > b?", a > b)      # compares if a is greater than b → False because 2 is not > 10
print("Is a < b?", a < b)      # compares if a is less than b → True because 2 < 10
print("Is a == b?", a == b)    # checks if a and b are equal → False

# What is smaller, c or d?
c = 2.02            # assigns floating-point value 2.02 to variable c
d = 2.01119999      # assigns floating-point value 2.01119999 to variable d

print("\nc:", c, "d:", d)           # prints both values on one line
print("Is c < d?", c < d)           # checks if c is less than d → False (2.02 is slightly bigger)
print("Is c > d?", c > d)           # checks if c is greater than d → True
print("Is c == d?", c == d)         # checks if c equals d → False because values are not identical

# what is bigger e or f?
e = float("inf")    # assigns positive infinity to e; float("inf") is treated as a very large number
f = 12912912912091228312903713582043754302895723048957   # a very large floating-point / integer number

print("\ne:", e, "f:", f)           # prints infinity vs the large number
print("Is e > f?", e > f)           # True because infinity is always larger than any real number
print("Is e < f?", e < f)           # False
print("Is e == f?", e == f)         # False because no real value equals infinity

# are these equal?
g = 1.02020202020      # assigns a floating-point number to g
i = 1.020202020201111  # assigns another floating-point number with more precision to i

print("\ng:", g, "i:", i)            # prints both floating-point values
print("Is g == i?", g == i)          # False because floating-point numbers differ slightly
print("Is g < i?", g < i)            # True because i has a slightly larger value
print("Is g > i?", g > i)            # False
