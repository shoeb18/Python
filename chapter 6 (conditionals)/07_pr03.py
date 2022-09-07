# find the spam comments in comment section

from distutils.errors import CompileError


comment = input("Enter comment : ")
spam = False

if ("make a lot of money" in comment):
    spam = True
elif ("buy now" in comment):
    spam = True
elif ("subscribe this" in comment):
    spam = True
elif ("click this" in comment):
    spam = True

if (spam):
    print("This is spam comment")
else:
    print("This is not a spam comment")
