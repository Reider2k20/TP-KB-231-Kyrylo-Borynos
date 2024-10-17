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

def operations(a):
    while True:
        b = str(input("Print your next number or print 'ex' to exit the program: "))

        if b != "ex":

            try:
                b = float(b)
            except ValueError:
                print("It's not a number")
                continue
            
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