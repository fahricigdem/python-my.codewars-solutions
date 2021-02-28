"""
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
"""

def filter_list(l):
    c=[]
    for i in range (len(l)):
        if type(l[i]) == int:
            c.append(l[i])
    return c


a=[1,2,'aasf','1','123',123]
print(filter_list(a))