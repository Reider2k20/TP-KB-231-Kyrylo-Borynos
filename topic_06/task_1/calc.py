from operations import enter, actions
from functions import sum, sub, mult, div, rdiv, deg
from datetime import datetime
import os



file_path = os.path.join(os.path.dirname(__file__), "Calc_Log.txt")

def calculation(a):
    while True:
        a_old = a
        b = enter()
        act = actions(a)

        match act:
            case "+":
                a = sum(a, b)
            case "-":
                a = sub(a, b)
            case "!-":
                a = sub(b, a)
            case "*":
                a = mult(a, b)
            case "/":
                a = div(a, b)
            case "!/":
                a = rdiv(a, b)
            case "^":
                a = deg(a, b)
            case "!^":
                a = deg(b, a)

        print("\nyour current result = ", a)
        with open(file_path, "a") as file:
            log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if not act:
                pass
            elif act in ["!-", "!/","!^"]:
                file.write(f"{log_time} | {b} {act[1]} {a_old} = {a}\n")
            else:
                file.write(f"{log_time} | {a_old} {act} {b} = {a}\n")



calculation(enter())