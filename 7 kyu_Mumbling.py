"""
https://www.codewars.com/users/fahricigdem/completed_solutions
Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
"""

def accum(s):
    text=''
    for i in range(len(s)):
        
        text+=s[i].upper()+s[i].lower()*i
        if i <len(s)-1:
            text=text+'-'
    return text

print(accum('dsadsa'))

