"""
likes([]) # must be "no one likes this"
likes(["Peter"]) # must be "Peter likes this"
likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"
"""
def likes(names):
    count=len(names)
    if count==0:
        return 'no one likes this'
    elif count==1:
        return "{} likes this".format(names[0])
    elif count==2:
        return "{} and {} like this".format(names[0],names[1])
    elif count==3:
        return "{}, {} and {} like this".format(names[0],names[1], names[2])
    elif count>3:
        return "{}, {} and {} others like this".format(names[0],names[1], len(names)-2)
    
print(likes(["Peter"]))