# write a program to find whether a given username contains less than 10 characters or not

username = input("Enter your username : ")

if (len(username) < 10):
    print("username is less than 10 characters")
else:
    print("username is greater than 10 characters")
