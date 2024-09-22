def enter():
    print("quadratic equation formula (X mean x^2): aX+bx+c")
    a = float(input('Enter your a: '))
    b = float(input('Enter your b: '))
    c = float(input('Enter your c: '))
    return a, b, c

def disc(a, b, c):
    D = b**2 - 4*a*c
    return D

a, b, c = enter()
print(disc(a, b, c))