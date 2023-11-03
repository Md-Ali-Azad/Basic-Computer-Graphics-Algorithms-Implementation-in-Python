def line_x_rectangle(a, b, x_min, y_min, x_max, y_max):

    # Intersections of f(x) = ax + b with the rectangle. (x, y, axis)
    p1, p2 = (x_min, a * x_min + b, 'x'), (x_max, a * x_max + b, 'x'),
    p3, p4 = ((y_min - b) / a, y_min, 'y'), ((y_max - b) / a, y_max, 'y')
    p1, p2, p3, p4 = sorted([p1, p2, p3, p4])
    print(p1,p2,p3,p4)
    if p1[2] == p2[2]:
        return None
    return p2[:2], p3[:2]


print(line_x_rectangle(8,9,1,2,9,8))
print(line_x_rectangle(6,8,3,6,6,10))