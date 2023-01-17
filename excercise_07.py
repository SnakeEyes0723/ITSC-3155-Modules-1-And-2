val = input('Enter a number or QUIT to quit: ')
entries = []
evenEntries = []
while(val != 'QUIT'):
    entries.append(int(val))
    val = input('Enter a number or QUIT to quit: ')
print('All numbers: ' + str(entries))
x = 0
while (x < len(entries)):
    if((entries[x] % 2) == 0):
        evenEntries.append(entries[x])
    x = x + 1
print('All even numbers: ' + str(evenEntries))
