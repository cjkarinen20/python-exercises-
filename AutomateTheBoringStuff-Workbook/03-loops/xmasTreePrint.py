import random

print('Enter the tree size: ')

treeSize = int(input())

for row_num in range(1, treeSize + 1):
    if random.randint(1, 4) == 1: 
        print( ' ' * (treeSize - row_num) + 'o' * (row_num * 2 - 1))
    else:
        print( ' ' * (treeSize - row_num) + '^' * (row_num * 2 - 1))
    
print((' ' * (treeSize - 1) + '#\n') * 2)