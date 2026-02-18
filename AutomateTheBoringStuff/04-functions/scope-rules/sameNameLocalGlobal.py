def spam():
    global eggs
    eggs = 'spam' # This is a global variable.
    
def bacon():
    eggs = 'bacon' # This is a local variable.

def ham():
    print(eggs) # This is the global variable.