import random

num = random.randint(1,10)

while True:
    guess = int(input('1Please enter guess: '))

    if guess == num:
        print('Nice Job. You are correct!')
        break
    else:
        print('Incorrect. Try again.')