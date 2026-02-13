import xmasTreePrint_for
import xmasTreePrint_while
import treePrint_for
import treePrint_while

def treePrint(treeType, loopType):
    if treeType == 'x':
        if loopType == 'f':
            xmasTreePrint_for.xmasTreePrint_for()
        elif loopType == 'w':
            xmasTreePrint_while.xmasTreePrint_while()
    elif treeType == 'p':
        if loopType == 'f':
            treePrint_for.treePrint_For()
        elif loopType == 'w':
            treePrint_while.treePrint_while()
    
if __name__ == "__main__":
    # This code only runs when the file is executed as a script
    print('Enter the type of tree to print. (X = Christmas Tree, P = Pine Tree) ')

    treeType = input().lower()
    
    print(f"treeType = {treeType}") #DEBUG
    
    if treeType == 'x' or treeType == 'p':
        
        print('Enter the type of loop to use. (F = for-loop, W = while-loop): ')
        
        loopType = input().lower()
        
        print(f"loopType = {loopType}") #DEBUG
        
        if loopType == 'f' or loopType == 'w':
            treePrint(treeType, loopType)
        
        else:
            print('Please enter a valid option (F or W).')
        
    else:
        print('Please enter a valid option (X or P).')

    
