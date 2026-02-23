import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    print(f"Guess: {guess}")
toss = random.randint(0, 1)  # 0 is tails, 1 is heads
if (toss == 1 and guess == "heads") or (toss == 0 and guess == "tails"): # User guessed correctly
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')