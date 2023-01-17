entries = []
uniqueEntries = []
val1 = int(input('Enter value 1: '))
entries.append(val1)
val2 = int(input('Enter value 2: '))
entries.append(val2)
val3 = int(input('Enter value 3: '))
entries.append(val3)
val4 = int(input('Enter value 4: '))
entries.append(val4)
val5 = int(input('Enter value 5: '))
entries.append(val5)
val6 = int(input('Enter value 6: '))
entries.append(val6)
val7 = int(input('Enter value 7: '))
entries.append(val7)
val8 = int(input('Enter value 8: '))
entries.append(val8)
val9 = int(input('Enter value 9: '))
entries.append(val9)
val10 = int(input('Enter value 10: '))
entries.append(val10)
print('Original List: ' + str(entries))
x = 0
y = 0
while(x < 10):
    while(y < 10):
        if(x != y):
            if(entries[x] == entries[y]):
                y = 10
            else:
                if(y == 9):
                    uniqueEntries.append(entries[x])
                    y = y + 1
                else:
                    y = y + 1
        else:
            y = y + 1
    y = 0
    x = x + 1
print('Numbers that appear once' + str(uniqueEntries))