friends = ['gaurav', 'vishal', 'ashwin', 'dipali', 'chetana']

name = input("Enter the name to check it present or not\n")

if (name in friends):
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")