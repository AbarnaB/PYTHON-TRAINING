import re
hand = open('mbox.txt')
search = input('Enter a regular expression: ')
count = 0
for line in hand:
    line = line.rstrip()
    if re.search(search, line): count = count + 1

print('mbox.txt had', count, 'lines that matched', search)
