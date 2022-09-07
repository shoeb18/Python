gamer = "game "
text = "programming"

# concatinate
print(gamer+text)

# string slicing
print(text[0:3]) # it slice the string from 0 to 2 index (yes! it excludes the last index)
print(text[0:]) # is same that text[0:11]
print(text[-8:]) # is same that text[3:11]

# note
# gamer[0] = 'f' # Error -->'str' object does not support item assignment


# string slicing with skip value
print(text[0::2]) # it prints the string skipping 1 character