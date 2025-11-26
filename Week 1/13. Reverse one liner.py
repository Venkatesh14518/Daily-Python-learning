# Reverse the string given below in a single line of code
# with the help of string slicing.

palindrome = "too bad i hid a boot" # the original string we want to reverse

reversed_string = palindrome[::-1] # [::-1] means: start to end, step -1 → moves backward, reversing the string

print(reversed_string)                # prints the reversed version of the sentence