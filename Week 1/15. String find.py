# Find the index of the first occurrence of the letter `n` in the string.

composer = "Ludvig van Beethoven"     # the string we are searching in

index_n = composer.find("n")          # .find("n") returns the index of the first 'n'; returns -1 if not found

print(index_n)                        # prints the position where 'n' first appears
