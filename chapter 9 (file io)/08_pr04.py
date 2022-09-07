from multiprocessing import context


with open("sample.txt") as f:
    content = f.read()

if "donkey" in content:
    content = content.replace("donkey","!@#$%")

print(content)

with open("sample.txt","w") as f:
    f.write(content)