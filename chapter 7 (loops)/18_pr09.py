# print the multiplication table in reverse order

n = int(input("Enter the number : "))
table = []


i = 0
while i<10:
    table.append((n*(i+1)))
    i=i+1
    
table.reverse()

for i in range(10):
    print(f"{table[i]}")