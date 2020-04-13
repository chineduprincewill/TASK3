import random

num = random.randint(1,9)
count = 0

while True:
    print('Enter your guess between 1 to 9')
    guess = input('>')
    if count == 5:
        print('You have exceeded your guess limit')
        break
    if guess != num:
        print('Wrong guess. Try again')
        count += 1
        continue
    if guess == num:
        print('Well guessed!')
        break
print('The answer is >>', num)
print('Done')