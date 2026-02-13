import random

def xmasTreePrint_for():
    print('Enter the tree size: ')

    treeSize = int(input())
    
    
    if treeSize < 1:
        print('Size must be greater than 0.')

    print('Xmas Tree Print - For-Loop: ') 
        
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



if __name__ == "__main__":
    # This code only runs when the file is executed as a script
    xmasTreePrint_for()