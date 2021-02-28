def get_middle(s):
    mid=len(s)//2
    if len(s) % 2 == 0:
        return s[mid-1:mid+1]
    else:
        return s[mid]
    

print(get_middle("of"))

"""
Test.assert_equals(get_middle("test"),"es")
Test.assert_equals(get_middle("testing"),"t")
Test.assert_equals(get_middle("middle"),"dd")
Test.assert_equals(get_middle("A"),"A")
Test.assert_equals(get_middle("of"),"of")
"""