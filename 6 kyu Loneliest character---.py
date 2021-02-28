import re
def loneliest(text):
    text = list(text.strip())
    if len(text) == 1:
        return text 
    voll=[]
    voll_wert=[]
    for i in range(len(text)):
        if re.match(r'[a-z]',text[i]):
            voll.append(text.index(text[i]))
            voll_wert.append(text[i])
    
    blank=[]
    for i in range (len(voll)-1, 0, -1):
        blank.append(voll[i]-voll[i-1]-1)
    blank.reverse()    
    
    for i in range(len(voll)):
        voll[i]=voll_wert[i]
        
    for i in range(1, len(voll)+len(blank), 2):
        voll.insert(i, blank[i//2])

    plus=[]
    for i in range(0, len(voll), 2):
        if i == 0:
            plus.append(voll[i+1])
        elif i == len(voll)-1:
            plus.append(voll[i-1])
        else:
            plus.append(voll[i-1] + voll[i+1])
    
    ergebnis=[]
    for i in range(len(plus)):
        if plus[i] == max(plus):
            ergebnis.append(i)

    for i in range(len(ergebnis)):
        ergebnis[i] = voll_wert[ergebnis[i]]
    
    return ergebnis
    


#print(loneliest('a b    c   o'))

print(loneliest('a')) #,['a'] )
print(loneliest('abc d   ef  g   h i j      ')) #, ['g'])
print(loneliest('a   b   c '))  #, ['b'])
print(loneliest('  abc  d  z    f gk s '))  #, ['z'])
print(loneliest('a  b  c  de  ')) #, ['b', 'c'])
print(loneliest('abc'))  #, ['a', 'b', 'c'])
