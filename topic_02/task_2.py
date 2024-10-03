def enter():
    a = float(input("Enter 1`st number: "))
    b = float(input("Enter 2`nd number: "))
    return a, b

def operations(a, b):
    while True:
        print("\n'+' — sum, '-' — sub, '*' — mult, '/' — div, '^' — deg")
        action = input("Select an action: ")
        if b == 0 and action == "/":
            print("can't be divided by 0")
        else:
            if action == "+":
                return a + b
            elif action == "-":
                return a - b
            elif action == "*":
                return a * b
            elif action == "/":
                return a / b
            elif action == "^":
                return a ** b
            else:
                print("This is not an action")


a, b = enter()
print(operations(a, b))