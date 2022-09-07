# create a hindi dictionary with english meaning


my_hindi_dict = {
    'chuha' : 'mouse',
    'khidki' : 'window',
    'kaichi' : 'scissor',
    'kitab' : 'book'
}

print("words are :", my_hindi_dict.keys())
word = input("Enter the hindi word : ")

print("The meaning in english :",my_hindi_dict.get(word))
