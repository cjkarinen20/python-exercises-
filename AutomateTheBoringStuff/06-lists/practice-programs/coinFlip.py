import random

number_of_streaks = 0


for experiment_number in range(10000):  # Run 100,000 experiments total.
    coinList = []
    # Code that creates a list of 100 'heads' or 'tails' values
    for i in range(100):
        toss = random.randint(0, 1)
        if toss == 1:
            coinList.append('H')
        elif toss == 0:
            coinList.append('T')
            
    # Code that checks if there is a streak of 6 heads or tails in a row
    for index, item in enumerate(coinList):
        coinSlice = coinList[index:index + 6]
        
        headStreak = ['H', 'H', 'H', 'H', 'H', 'H']
        tailStreak = ['T', 'T', 'T', 'T', 'T', 'T']
        
        if coinSlice == headStreak:
            number_of_streaks += 1
        elif coinSlice == tailStreak:
            number_of_streaks += 1
            
print('Chance of streak: %s%%' % (number_of_streaks / 100))
