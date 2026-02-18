
# 1.) Code that is in the global scope, outside all 
# functions, can't use local variables. (See 'README')

def spam():
    eggs ='sss'
    
spam()
print(eggs)