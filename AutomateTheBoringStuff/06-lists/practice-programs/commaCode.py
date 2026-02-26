
def listString(list):
    
    commaList = []
    
    if list[0] == None:
        return ' '
    
    for index, item in enumerate(list):
        commaList.append(item)
        if index < len(list) - 2:  
            commaList.append(', ')
        elif index == len(list) - 2:
            commaList.append(', and ')
        elif index == len(list) - 1:
            break  
        
    commaStr = ''
    commaStr = commaStr.join(commaList)
    return commaStr

letters = ['a', 'b', 'c', 'd', 'e']
print(listString(letters))