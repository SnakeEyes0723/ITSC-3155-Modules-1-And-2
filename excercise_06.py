# For this code, I had to figure out how to print on the same line. I used this website to help me:
# https://www.tutorialspoint.com/how-to-print-in-same-line-in-python#:~:text=Modify%20print()%20method%20to,printed%20in%20the%20same%20line.
row = int(input('Enter a row number between 1 and 5: '))
if(row < 1 or row > 5):
    print('Invalid input. The row number must be between 1 and 5, try again.')
column = int(input('Enter a column number between 1 and 5: '))
if(column < 1 or column > 5):
    print('Invalid input. The column number must be between 1 and 5, try again.')
x = 0
y = 0
while (x < 5):
    while (y < 5):
        if(x == (row - 1) and y == (column - 1)):
            print('1', end= ' ')
            y = y + 1
        else:
            print('0', end= ' ')
            y = y + 1
    print('')
    y = 0
    x = x + 1