with open("sample.txt","r") as f:
    a = f.read()
print(a)

with open("sample.txt","w") as f:
    a = f.write("Hi I'm coder")
print(a)
