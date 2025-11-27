# Use a Python string method to prove which of the following files
# are .pdf files, and which aren't.
# Call the method on each file string and print() Python's response.

file_1 = "operators.pdf"            # file ending in .pdf
file_2 = "snowfall.jpg"             # file ending in .jpg
file_3 = "uncle-joes-wedding.doc"   # file ending in .doc
file_4 = "invitation.pdf"           # file ending in .pdf

# We use the string method .endswith(".pdf")
# This checks whether the string finishes with the substring ".pdf"
# It returns True if it does, False if it doesn't.

print(file_1.endswith(".pdf"))    # True → because "operators.pdf" ends with ".pdf"
print(file_2.endswith(".pdf"))    # False → it's a .jpg file
print(file_3.endswith(".pdf"))    # False → it's a .doc file
print(file_4.endswith(".pdf"))    # True → it ends with ".pdf"
