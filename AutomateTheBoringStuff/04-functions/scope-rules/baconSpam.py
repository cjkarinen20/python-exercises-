
# 2.) Code that is in one function’s local scope can’t
# use variables in any other local scope. (See 'README')

def spam():
    eggs='SPAMSPAM'
    bacon()
    print(eggs) # Prints 'SPAMSPAM'
    
def bacon():
    ham = 'hamham'
    eggs = 'BACONBACON'
    
spam()