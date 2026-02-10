print('Enter the tree size: ')

treeSize = int(input())

for row_num in range(1, treeSize + 1):
    print( ' ' * (treeSize - row_num) + '^' * (row_num * 2 - 1))
    
print((' ' * (treeSize - 1) + '#\n') * 2)