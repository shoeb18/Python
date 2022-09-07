# write a function to remove the word from string and strip the string
def remove_and_strip(string, word):
    new_str = string.replace(word,"")
    return new_str.strip()


text = "         Hello, how are you my name is shoeb"

s = remove_and_strip(text,'shoeb')
print(text)
print(s)