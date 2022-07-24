import os
while True:
    filepath = input("Enter full file path with name and extension: ")
    if os.path.exists(filepath):
        break
    print("File does not exists.")
with open(filepath) as file:
    contents = file.read()
    print("\n"+" FILE CONTENTS ".center(25,"#"),"\n")
    print(contents)
    print("#"*25,"\n")
    print("Count".center(12,"-"),"\n")
    count = {}
    for char in contents:
        count.setdefault(char, 0)
        count[char] += 1
    count.pop("\n")
    for key, value in count.items():
        print(key.ljust(8,".")+str(value).rjust(4))