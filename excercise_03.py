val = int(input('Enter a number greater than 1: '))
if val < 1:
    print('This value is not greater than one. Try again.')
else:
    while(val >= 0):
        print('The cube of ' + str(val) + ' is ' + str(val*val*val))
        val = val - 1
