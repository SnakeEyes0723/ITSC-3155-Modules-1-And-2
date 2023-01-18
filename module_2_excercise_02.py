upperCaseletters = []
lowerCaseLetters = []
val = input("Enter a string: ")
x = 0
while(x < len(val)):
    if val[x] == " ":
        x = x + 1
    if val[x].isupper():
        upperCaseletters.append(val[x])
        x = x + 1
    if val[x].islower():
        lowerCaseLetters.append(val[x])
        x = x + 1
finalString = ""
y = 0
while(y < len(lowerCaseLetters)):
    finalString = finalString + lowerCaseLetters[y]
    y = y + 1
z = 0
while(z < len(upperCaseletters)):
    finalString = finalString + upperCaseletters[z]
    z = z + 1
print(finalString)
