def enter():
    a = float(input("Print your number: "))
    return a

def operations(a):
    while True:
        b = str(input("Print your next number or print 'ex' to exit the program: "))

        if b != "ex":

            b = float(b)
            print("\nPS — with values position swap \n'+' — sum, '-' — sub, '!-' — sub (PS), '*' — mult, '/' — div, '!/' — div (PS), '^' — deg, '!^' — deg (PS), or 'ex' to exit the program")
            action = input("Select an action: ")

            match action:
                case "+":
                    a += b
                case "-":
                    a -= b
                case "!-":
                    a = b - a
                case "*":
                    a *= b
                case "/":
                    if b == 0:
                        print("can't be divided by 0, please enter your next number not equal to 0")
                    else:
                        a /= b
                case "!/":
                    if a == 0:
                        print("can't be divided by 0, now you result equal to 0, try another action")
                    else:
                        a = b / a
                case "^":
                    a **= b
                case "!^":
                    a = b ** a
                case "ex":
                    print("\nyour current result = ", a)
                    exit(0)
                case _:
                    print("This is not an action")

            print("\nyour current result = ", a)


        else:
            print("your current result = ", a)
            exit(0)


a = enter()
operations(a)