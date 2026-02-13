

def treePrint_For():
    print('Enter the tree size: ')

    treeSize = int(input())
    
    if treeSize < 1:
        print('Size must be greater than 0.')

    print('Pine Tree Print - For-Loop: ')
        
    for row_num in range(1, treeSize + 1):
        print( ' ' * (treeSize - row_num) + '^' * (row_num * 2 - 1))
        
    print((' ' * (treeSize - 1) + '#\n') * 2)


    
if __name__ == "__main__":
    # This code only runs when the file is executed as a script
    treePrint_For()