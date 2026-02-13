def treePrint_while():
    print('Enter the tree size: ')

    treeSize = int(input())

    if treeSize < 1:
        print('Size must be greater than 0.')

    row_num = 0
    
    print('Pine Tree Print - While Loop: ')
    
    while row_num <= treeSize:
        print( ' ' * (treeSize - row_num) + '^' * (row_num * 2 - 1))
        row_num += 1

        
    print((' ' * (treeSize - 1) + '#\n') * 2)



if __name__ == "__main__":
    # This code only runs when the file is executed as a script
    treePrint_while()