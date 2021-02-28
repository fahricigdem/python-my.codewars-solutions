"""
Task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith,
but they are not capitalized in the same way he originally typed them.
"""
def to_jaden_case(string):
    a=string.split()
    a=[i.capitalize() for i in a]
    a = " ".join(a)
    return a

print(to_jaden_case('dasdas adas dsa'))