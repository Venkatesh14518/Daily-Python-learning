# 1) Initialize variable a to true, b to false and c to true
a = True      # a is True
b = False     # b is False
c = True      # c is True

# 2) If you print(a and b or c) what will it return? Why?
print(a and b or c)        # 'and' evaluates first → (a and b) becomes False, then False or c → c is True, so result = True

# Does the order of operations matter?
# Yes, because 'and' is always evaluated before 'or'

# 3) Is print(a or b and c) different?
print(a or b and c)        # 'and' still evaluates first → (b and c) = False, so expression becomes a or False → result = True

# 4) Assign c to false and print the value of a and b or c
c = False                  # c becomes False now
print(a and b or c)        # first (a and b) = False, then False or c = False → result = False

# Understand the difference in each scenario
# The results change because the value of c changes, and because 'and' executes before 'or'

# What is happening here?
# Python evaluates 'and' first, then 'or'

# 5) Now try to use some ()'s to force python to evaluate it differently.
print(a and (b or c))      # parentheses change the order: first (b or c) = False, then a and False = False
print((a and b) or c)      # another grouping: first (a and b) = False, then False or c = False


