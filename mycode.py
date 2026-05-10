def solve_2x2(x_1, y_1, t1, x_2, y_2, t2):
    A = x_1*y_2 - x_2*y_1
    x1 = t1*y_2 - t2*y_1
    x2 = x_1*t2 - x_2*t1
    x_val = round(x1/A, 3)
    y_val = round(x2/A, 3)
    return f"x={x_val}, y={y_val}"


def solve_3x3(x_1,y_1,z_1,t1,x_2,y_2,z_2,t2,x_3,y_3,z_3,t3):
    A = x_1*(y_2*z_3-y_3*z_2)
    B = -x_2*(y_1*z_3-y_3*z_1)
    C = x_3*(y_1*z_2-y_2*z_1)
    A_total = A+B+C

    x1 = t1*(y_2*z_3-y_3*z_2)
    x2 = -x_2*(t2*z_3-y_3*t3)
    x3 = x_3*(t2*z_2-y_2*t3)
    x = x1+x2+x3

    y1 = x_1*(t2*z_3-z_2*t3)
    y2 = -t1*(y_1*z_3-y_3*z_1)
    y3 = x_3*(y_1*t3-t2*z_1)
    y = y1+y2+y3

    z1 = x_1*(y_2*t3-t2*z_2)
    z2 = -x_2*(y_1*t3-t2*z_1)
    z3 = t1*(y_1*z_2-y_2*z_1)
    z = z1+z2+z3

    return f"x={round(x/A_total,3)}, y={round(y/A_total,3)}, z={round(z/A_total,3)}"