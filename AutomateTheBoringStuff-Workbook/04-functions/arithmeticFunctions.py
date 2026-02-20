
def plus_one(number):
    return number + 1

def add(number1, number2):
    total_sum = number1
    for i in range(number2):
        total_sum = plus_one(total_sum)
    return total_sum

def multiply(number1, number2):
    total_sum = number1
    for i in range(number2):
        total_sum = add(total_sum)
    return total_sum