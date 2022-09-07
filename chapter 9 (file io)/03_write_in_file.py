f = open("sample.txt","a") # it writes in file at the end
# f = open("sample.txt","w") # it writes in file and override before content

text = input("Write something: ")

f.write(text)
f.close()