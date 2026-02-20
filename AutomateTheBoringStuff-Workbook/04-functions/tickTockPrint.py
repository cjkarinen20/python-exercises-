import time

def tickTock(seconds):
    itr = 1
    while itr <= seconds:
        if itr % 2 == 1: #i is odd
            print('Tick...')
            time.sleep(1)
        if itr % 2 == 0: #i is even
            print('Tock...')
            time.sleep(1)
        itr += 1
        
            
