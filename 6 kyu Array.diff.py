def array_diff(a, b):
    for i in range (len(a)):
        for j in range (len(b)):
            if b[j] in a:
                a.remove(b[j])
    return a

x=[16, 11, 16, -19, 0, -13, 3, 20, 11]
y=[-11, -11, -11, 11, 20, 15, -6, 20, -13, -3, 19, -6]

print(array_diff(x, y))