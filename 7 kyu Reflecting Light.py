"""
Four mirrors are placed in a way that they form a rectangle with corners at coordinates (0, 0), (max_x, 0), (0, max_y),
and (max_x, max_y). A light ray enters this rectangle through a hole at the position (0, 0) and moves at an angle of 45
degrees relative to the axes. Each time it hits one of the mirrors, it gets reflected. In the end, the light ray hits one
of the rectangle's corners, and flies out. Your function must determine whether the exit point is either (0, 0) or
(max_x, max_y). If it is either (0, 0) or (max_x, max_y), return True and False otherwise.
Example:
For max_x = 10 and max_y = 20, the ray goes through the following lattice points: (1, 1), (2, 2), (3, 3), (4, 4),
(5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (9, 11), (8, 12), (7, 13), (6, 14), (5, 15), (4, 16), (3, 17),
(2, 18), (1, 19), (0, 20).
The ray left the rectangle at position (0, 20), so the result is False.
"""

def reflections(max_x, max_y):
    x=y=0
    Light=state1=True
    state2=state3=state4=False
    END=None
    while Light:
        if state1:
            x+=1
            y+=1
            if x == max_x and y == max_y: return True
            elif x==max_x: state1,state2=False,True
            elif y==max_y: state1,state4=False,True
        if state2:
            x-=1
            y+=1
            if x == 0 and y == max_y: return False
            elif x==0: state2,state1=False,True
            elif y==max_y:state2,state3=False,True
        if state3:
            x-=1
            y-=1
            if x == 0 and y == 0:return True
            elif x==0: state3,state4=False,True
            elif y==0: state3,state2=False,True
        if state4:
            x+=1
            y-=1
            if x == max_x and y == 0: return False
            elif x==max_x:state4,state3=False,True
            elif y==0: state4,state1=False,True

print(reflections(12, 23))
print(reflections(10, 20))
print(reflections(10, 30))