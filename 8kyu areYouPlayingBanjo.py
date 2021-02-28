def areYouPlayingBanjo(name):
    if name[0] in ('R','r'):
        return f'{name} play banjo'
    else: return f'{name} does not playbanjo'
    
    
print(areYouPlayingBanjo('Rubby'))
print(areYouPlayingBanjo('tubby'))
print(areYouPlayingBanjo('Tubby'))

