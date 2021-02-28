def spacey(array):
    arrayOutput=[]
    j=''
    for i in array:
        j+=i
        arrayOutput.append(j)
    return arrayOutput


print(spacey(['kevin', 'has','no','space']))