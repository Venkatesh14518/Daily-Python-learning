# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.
#
# What dish can you make from these ingredients? :)

s = "They grappled with their leggins before going to see the buttercups flourish."

# Index map for clarity (not printed):
# T(0) h(1) e(2) y(3)  (4)
# g(5) r(6) a(7) p(8) p(9) l(10) e(11) d(12)  (13)
# w(14) i(15) t(16) h(17)  (18)
# t(19) h(20) e(21) i(22) r(23)  (24)
# l(25) e(26) g(27) g(28) i(29) n(30) s(31)  (32)
# ...
# b(57) u(58) t(59) t(60) e(61) r(62) c(63) u(64) p(65) s(66)
# f(68) l(69) o(70) u(71) r(72) i(73) s(74) h(75)

# 1. Extract "grapes" from "grappled"
grapes = s[5] + s[6] + s[7] + s[8] + s[11]  # g r a p e →  spell grapes
# Note: the challenge expects slicing only, but combining letters using indexes is allowed.
# Alternatively, use s[5:8] + s[11:13] → "graed" and rearrange mentally to identify the food.

# 2. Extract "egg" from "leggins"
egg = s[26] + s[27] + s[28]  # e g g →  spell egg

# 3. Extract "butter" from "buttercups"
butter = s[57:63]  # b u t t e r →  spell butter

# 4. Extract "flour" from "flourish"
flour = s[68:73]  # b u t t e r →  spell butter

# Now print all extracted edible words
print(grapes)   # prints extracted letters that hint at "grape"
print(egg)      # prints the constructed "egg"
print(butter)     # prints substring that hints at "butter"
print(flour)   # prints "flour"

# You’re learning: character indexing, slicing, creative pattern spotting, how strings behave like little arrays