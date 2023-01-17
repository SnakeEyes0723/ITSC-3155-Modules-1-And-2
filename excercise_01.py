# For this excercise and future ones, I had to look up a few things about, like assigning and casting variables, inputs,
# how to use operators, and if, elif, and else statements. The links for websites that helped me are listed here:
# https://www.geeksforgeeks.org/taking-input-in-python/, https://www.programiz.com/python-programming/if-elif-else
# https://www.geeksforgeeks.org/relational-operators-in-python/, https://www.w3schools.com/python/python_variables.asp
val = int(input('Enter a number grade from 0 to 100:'))
if val >= 0 and val < 60:
    print('You have an F.')
elif val >= 60 and val < 70:
    print('You have an D.')
elif val >= 70 and val < 80:
    print('You have an C.')
elif val >= 80 and val < 90:
    print('You have an B.')
elif val > 89 and val <= 100:
    print('You have an A.')
else:
    print('This input cannot be graded. Enter a different value.')