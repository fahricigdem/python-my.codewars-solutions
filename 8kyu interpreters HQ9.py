def HQ9(code):
    if code == 'H':
        return 'Hello World!'
    elif code == 'Q':
        return 'Q'
    elif code == '9' :
        text = ''
        for i in range (99, 2, -1):
            text += str(i)+' bottles of beer on the wall, '+str(i)+' bottles of beer.\n'+'Take one down and pass it around, '+str(i-1)+' bottles of beer on the wall.\n'
        text += '2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n'
        text += '1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.'
        return text    
    
    
print(HQ9('9'))
