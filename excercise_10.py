letters = []
listOfLists = []
entry = input('Enter a string: ')
x = 0
while(x < len(entry)):
    if((x+2) < len(entry)):
        letters = [entry[x], entry[x+1], entry[x+2]]
        listOfLists.append(letters)
    elif((x+1) < len(entry)):
        letters = [entry[x], entry[x+1]]
        listOfLists.append(letters)
    else:
        letters = [entry[x]]
        listOfLists.append(letters)
    x = x + 3
print(str(listOfLists))


