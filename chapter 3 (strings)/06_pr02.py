# write a program to fill in a letter template given below with name and data

letter = '''Dear <|name|>,
            We are very happy to tell you
You are selected, In Rockstar Studios As
Lead Game Programmer.
                        Date : <|date|>
                        Thanks juily from rockstar'''
                            
name = input("Enter your name : ")
date = input("Enter the date : ")

letter = letter.replace('<|name|>',name)
letter = letter.replace('<|date|>',date)

print(letter)

            