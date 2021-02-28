def killer(suspect, dead):
    a=[[x,suspect[x]] for x in suspect]
    killer = [0]*len(a)
    for i in range(len(a)):
        for k in range(len(dead)):
                if dead[k] in a[i][1]: killer [i] += 1
        if killer[i] == len(dead): return a[i][0]

print(killer({'James': ['Jacob'],
 'Johnny': ['David', 'Kyle', 'Lucas','Bill'],
 'Peter': ['Lucy', 'Kyle', 'Bill', 'Lucas','Jacob']},['Lucas', 'Bill','Jacob']))



