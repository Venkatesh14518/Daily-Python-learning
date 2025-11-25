# can you figure out the logic here?

ay = "a"         # variable ay stores the character "a" as a string
bee = "b"        # variable bee stores the character "b" as a string

# which one is bigger?
print(ay > bee)  # compares "a" and "b"; returns False because Python checks their Unicode values
print(ay < bee)  # returns True because the Unicode value of "a" is less than the Unicode value of "b"
print(ay == bee) # returns False because "a" and "b" are not the same character

# why??
print(ord(ay))   # ord() converts a character to its Unicode (ASCII) number — "a" becomes 97
print(ord(bee))  # ord() converts "b" to its Unicode (ASCII) number — "b" becomes 98
# Python compares letters using their Unicode values, so since 97 < 98 → "a" < "b"

# here is a hint: check out the ord() function
# How does python store string characters under the hood?
# look up what ord() does online and report back!

# extra helpful demonstration:
print(chr(97))   # chr() converts a Unicode number back to its character — 97 becomes "a"
print(chr(98))   # chr() converts 98 back to "b"
# chr() is the opposite of ord(), showing clearly how numbers and letters are linked internally
