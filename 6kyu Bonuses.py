def bonus(arr, s):
    import math
    lcm = arr[0]
    for i in range(1, len(arr)):
        lcm *= arr[i]//math.gcd(lcm, arr[i])

    b=sum([math.ceil(lcm/i) for i in arr])
    print([((lcm*s/b)/i) for i in arr])
    
    return ([math.ceil((lcm*s/b)/i) for i in arr])


print(bonus([25, 22, 15, 22, 22], 5213))

