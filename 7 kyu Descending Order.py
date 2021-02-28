"""
Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
"""

def descending_order(num):
    a=[int(x) for x in str(num)]

    for i in range (len(a)):
        for j in range (i):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]

    strings = [str(integer) for integer in a]
    a_string = "".join(strings)
    an_integer = int(a_string)        
        
    return (an_integer)

print(descending_order(334325353))

