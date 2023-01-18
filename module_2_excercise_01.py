letters = []
val = input("Enter a string to be reversed: ")
x = len(val) - 1
while(x >= 0):
    letters.append(val[x])
    x = x - 1
y = 0
reversedString = ""
while(y < len(letters)):
    reversedString = reversedString + letters[y]
    y = y + 1
print(str(reversedString))