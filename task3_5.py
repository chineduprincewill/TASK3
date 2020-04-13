print('Enter first integer')
first = input('>')
print('Enter second integer')
second = input('>')

try:
    total = int(first) + int(second)
    if total in range(15, 21):
        total = 20
    print('Sum is ',total)
except:
    print('Values are not integers!')
