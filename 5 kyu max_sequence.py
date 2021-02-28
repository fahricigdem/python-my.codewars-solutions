def max_sequence(a):
    maxi = []
    for i in range (len(a)-1):
        for j in range (i+1,len(a)+1): 
            maxi.append(a[i:j])
    max_sum=0
    for i in range(len(maxi)):
        if sum(maxi[i]) > max_sum:
            max_sum = sum(maxi[i])
    return max_sum

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

