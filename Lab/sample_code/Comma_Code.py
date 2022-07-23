def itemList(list):
    string = str(list[0])
    for i in range(1,len(list)-1): 
        string = string + " , " + str(list[i])
    string = string + " and " + str(list[-1])
    return string


spam = ["apples", "bananas", "tofu", "cats"]
listagem = itemList(spam)
print(listagem)
