
def collatz(number):
        
    if number % 2 == 0: # Input is even
        return number // 2
            
    elif number % 2 == 1: # Input is odd
        return 3 * number + 1
    
    
print('Enter an integer: ')
    
userInput = int(input())
    
result = collatz(userInput)

while result != 1:

    print(result, end=" ")
    result = collatz(result)

        
        