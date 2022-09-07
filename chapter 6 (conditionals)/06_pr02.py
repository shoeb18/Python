# calcualte student percentage in 3 subject and print result

sub1 = int(input("Enter the marks of subject 1 : "))
sub2 = int(input("Enter the marks of subject 2 : "))
sub3 = int(input("Enter the marks of subject 3 : "))

percentage = (sub1+sub2+sub3)/3

print("Congratulations! your percentage is:",percentage)

if (percentage >= 35 and sub1 > 34 and sub2 > 34 and sub3 > 34):
    print("You are pass!")
else:
    print("You are fail!")