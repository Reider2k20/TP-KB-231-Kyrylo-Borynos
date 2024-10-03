def enter():
    print("quadratic equation formula (X mean x^2): aX+bx+c")
    a = float(input('Enter your a: '))
    b = float(input('Enter your b: '))
    c = float(input('Enter your c: '))
    return a, b, c

def disc(a, b, c):
    D = b**2 - 4*a*c
    return D

def roots(a, b, D):
    if D > 0:
        x1 = (-b + D**0.5)/(2*a)
        x2 = (-b - D**0.5)/(2*a)
        ans = "x1 = " + str(x1) + "\nx2 = " + str(x2)
    elif D == 0:
        x = (-b)/(2*a)
        ans = "discriminant is 0, x = " + str(x)
    else:
        ans = "discriminant is less than 0, the equation has no roots"
    return ans



a, b, c = enter()
d = disc(a, b, c)
print(roots(a, b, d))