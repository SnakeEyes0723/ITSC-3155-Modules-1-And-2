entries1 = []
entries2 = []
common = []
val11 = int(input('Enter the first integer of the first list: '))
entries1.append(val11)
val12 = int(input('Enter the second integer of the first list: '))
entries1.append(val12)
val13 = int(input('Enter the third integer of the first list: '))
entries1.append(val13)
val14 = int(input('Enter the fourth integer of the first list: '))
entries1.append(val14)
val15 = int(input('Enter the fifth integer of the first list: '))
entries1.append(val15)
val21 = int(input('Enter the first integer of the second list: '))
entries2.append(val21)
val22 = int(input('Enter the second integer of the second list: '))
entries2.append(val22)
val23 = int(input('Enter the third integer of the second list: '))
entries2.append(val23)
val24 = int(input('Enter the fourth integer of the second list: '))
entries2.append(val24)
val25 = int(input('Enter the fifth integer of the second list: '))
entries2.append(val25)
print('List 1: ' + str(entries1))
print('List 2: ' + str(entries2))
x = 0
y = 0
while(x < 5):
    while(y < 5):
        if(entries1[x] == entries2[y]):
            common.append(entries2[y])
            y = y + 1
        else:
            y = y + 1
    y = 0
    x = x + 1
print('Common List: ' + str(common))
        