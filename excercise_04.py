# For this code and future ones, I had to learn how to create a list in Python, which I learned from this website:
# https://www.programiz.com/python-programming/list
n = int(input('Enter the number of items in the list: '))
entries = []
val = 1
while(val <= n):
    entry = float(input('Enter a number: '))
    entries.append(entry)
    val = val + 1
print('List: ' + str(entries))
averageCount = 0
average = 0
while (averageCount < n):
    average = average + entries[averageCount]
    averageCount = averageCount + 1
average = average / n
print('Average: ' + str(average))