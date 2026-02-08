print('Enter an integer:')

userInput = int(input())

if userInput % 3 == 0 and userInput % 5 == 0:
    print('Fizz Buzz')
    
elif userInput % 3 == 0 or userInput % 5 == 0:
    if userInput % 3 == 0:
        print('Fizz ')
    elif userInput % 5 == 0:
        print('Buzz ')

else:
    print(str(userInput))