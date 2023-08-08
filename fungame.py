import random

num = random.randint(1,10)

while True:
    guess = int(input('Please enter guess between 1 and 10: '))

    if guess == num:
        print('Nice Job. You are correct!')
        break
    else:
        print('Incorrect. Try again.')