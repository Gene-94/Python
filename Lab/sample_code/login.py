while True:
    print("Who are you?")
    name = input()
    if name != 'Yev':
        print("I don't know any", name+". Get out of here!")
        continue
    print("Hello master", name+". Do you have the key?")
    password = input("secret key: ")
    if password != 'thesecret':
        print("Have you lost the key master? Are you really", name+"?")
    else:
        break
print("Wellcome master", name+", the gates are open for you.")