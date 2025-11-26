# Use string indexing and string concatenation (or f-strings)
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers " # the string we will pick letters from; note the trailing space

# Let's inspect the indexes so we know where each letter sits.
# t(0), w(1), e(2), e(3), z(4), e(5), r(6), s(7), space(8)

# We need to build: "we see trees"
# Break it down:  w e   s e e   t r e e s

# First word: "we"
first_word = word[1] + word[2] # word[1] = 'w', word[2] = 'e'

# Second word: "see"
second_word = word[7] + word[2] + word[2] # 's' + 'e' + 'e'

#Third word: "trees"
third_word = word[0] + word[6] + word[2] + word[2] + word[7] # t + r + e + e + s

# Now assemble the final sentence
sentence = first_word + " " + second_word + " " + third_word

print(sentence) # prints: we see trees

# This exercise secretly teaches indexing concatenation, string construction, logic




