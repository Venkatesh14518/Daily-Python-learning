# Which of the following strings is the longest?
# Use the len() function to find out.
# You can run `len(my_variable)` and it will return the len of the variable (in this case it's a string)

longest_german_word = "Donaudampfschifffahrtsgesellschaftskapitänskajütentürschnalle"
longest_hungarian_word = "Megszentségteleníthetetlenségeskedéseitekért"
longest_finnish_word = "Lentokonesuihkuturbiinimoottoriapumekaanikkoaliupseerioppilas"
strong_password = "%8Ddb^ca<*'{9pur/Y(8n}^QPm3G?JJY}\(<bCGHv^FfM}.;)khpkSYTfMA@>N"

# Find the lengths of each string using len()
german_length = len(longest_german_word)      # len() is a built-in function that COUNTs characters in a string → result is stored in a new variable
hungarian_length = len(longest_hungarian_word) # stores the character count of the Hungarian word
finnish_length = len(longest_finnish_word)    # stores the character count of the Finnish word
password_length = len(strong_password)        # stores the character count of the password string


# Determine which one is longest using max()
longest_length = max(german_length, hungarian_length, finnish_length, password_length)  # max() returns the BIGGEST number from the values given

# Now identify *which* variable has that length
# Below begins a decision structure:
# if / elif / else chooses which block of code to run based on True/False logic
# "=" means assignment (put a value into a variable)
# "==" means comparison ("is this equal to that?")
if longest_length == german_length:                                # checks if longest_length matches german_length (True or False)
    longest_name = "longest_german_word"                           # runs only if the above comparison is True; assigns text to variable longest_name
    longest_string = longest_german_word                            # stores the actual German word as the winning string
elif longest_length == hungarian_length:                           # elif means "else if" → only checked if previous condition was False
    longest_name = "longest_hungarian_word"                        # assigns the name of the winning variable
    longest_string = longest_hungarian_word                         # stores the Hungarian string as winner
elif longest_length == finnish_length:                             # checked only if both previous comparisons were False
    longest_name = "longest_finnish_word"                          # assigns Finnish variable name as winner
    longest_string = longest_finnish_word                           # stores the Finnish string as winner
else:                                                              # runs if NONE of the above comparisons were True → meaning the password must be longest
    longest_name = "strong_password"                               # assigns password variable name as winner
    longest_string = strong_password                               # stores the actual password string as winner


# Now that you know what the longest word is, print it out in an f-string below
print(f"The longest string is {longest_name} with length {longest_length}.")  # f-string inserts variable values inside {} directly into the sentence

# Print the result in an f-string
print(f"It looks like this: {longest_string}")                                # prints the actual content of the longest string