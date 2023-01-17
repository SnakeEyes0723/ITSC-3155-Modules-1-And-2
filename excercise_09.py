words = []
word1 = input('Enter the first word: ')
words.append(word1)
word2 = input('Enter the second word: ')
words.append(word2)
word3 = input('Enter the third word: ')
words.append(word3)
word4 = input('Enter the fourth word: ')
words.append(word4)
word5 = input('Enter the fifth word: ')
words.append(word5)
print('Words: ' + str(words))
print('One String: ')
x = 0
while (x < 5):
    print(words[x], end= " ")
    x = x + 1
