# For this code and future ones, I had to look up how to use the operator 'in', so I had help from this website:
# https://www.digitalocean.com/community/tutorials/python-check-if-string-contains-another-string
word1 = input('Enter the first string: ')
word2 = input('Enter the second string: ')
if (word1 in word2 or word2 in word1):
    print('True')
else:
    print('False')
