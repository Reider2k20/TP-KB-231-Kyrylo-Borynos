def enter():
    while True:
        a = input("To exit the program — print 'ex' \nPrint your number: ")
        if a != "ex":
            try:
                a = float(a)
            except ValueError:
                print("It's not a number\n")
                continue
            return a
        else:
            exit(0)

def actions(a):
    print("\nPS — with values position swap \n'+' — sum, '-' — sub, '!-' — sub (PS), '*' — mult, '/' — div, '!/' — div (PS), '^' — deg, '!^' — deg (PS), or 'ex' to exit the program")
    action = input("Select an action: ")
    if action == "ex":
        print("\nyour current result = ", a)
        exit(0)
    elif action in ["+", "-", "!-", "*", "/", "!/", "^", "!^"]:
        return action
    else:
        print("This is not an action")
