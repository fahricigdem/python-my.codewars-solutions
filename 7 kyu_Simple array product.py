"""
Examples:
solve( [[1, 2],[3, 4]] ) = 8. The max product is given by 2 * 4
solve( [[10,-15],[-1,-3]] ) = 45, given by (-15) * (-3)
solve( [[1,-1],[2,3],[10,-100]] ) = 300, given by (-1) * 3 * (-100)
"""
import itertools

def solve(arr):
    minmax = [[min(i), max(i)] for i in arr]    

    multis=[]
    for i in itertools.product(*minmax):
        multi=1
        for j in i:
            multi*=j
        multis.append(multi)

    return max(multis)

print(solve( [[1, 2],[3, 4]]))