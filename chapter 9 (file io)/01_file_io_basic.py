# use open function to read the content of a file ! 
# f = open("file.txt", "r") # by default the mode is r
f = open("file.txt") # by default the mode is r

data = f.read(5) # it read first 5 characters from the file
print(data)
f.close()