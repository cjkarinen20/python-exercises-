import random

print('Enter the tree size: ')

treeSize = int(input())

for row_num in range(treeSize):
    
    spaces = " " * (treeSize - row_num - 1)
    row = ""
    for _ in range(2 * row_num + 1):
            if random.randint(1, 4) == 1:
                row += "o"
            else:
                row += "^"

    print(spaces + row)
            
print((' ' * (treeSize - 1) + '#\n') * 2)