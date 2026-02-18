
# 3.) Code in a local scope can access 
# global variables. (See 'README')

def spam():
    print(eggs) # Prints 'GLOBALGLOBAL'
eggs = 'GLOBALGLOBAL'
spam()
print(eggs)