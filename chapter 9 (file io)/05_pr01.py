f = open("poem.txt")

text = f.read()

if "twinkle" in text:
    print("twinkle is present")
else:
    print("twinkle is not present")

f.close()