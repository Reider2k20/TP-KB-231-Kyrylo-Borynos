from operations import Operations
from functions import Functions
from logging import Logger



class Calc:
    def __init__(self):
        self.functions = Functions()
        self.operations = Operations()
        self.logger = Logger()
    
    def wr_log(self, a, b, act, a_old):
        self.logger.log(a, b, act, a_old)

    def calculation(self):
        a = self.operations.enter()
        while True:
            a_old = a
            b = self.operations.enter()
            act = self.operations.actions(a)

            match act:
                case "+":
                    a = self.functions.sum(a, b)
                case "-":
                    a = self.functions.sub(a, b)
                case "!-":
                    a = self.functions.sub(b, a)
                case "*":
                    a = self.functions.mult(a, b)
                case "/":
                    if b == 0:
                        print("can't be divided by 0, please enter your next number not equal to 0\n")
                        continue
                    a = self.functions.div(a, b)
                case "!/":
                    if a == 0:
                        print("can't be divided by 0, now you result equal to 0, try another action\n")
                        continue
                    a = self.functions.div(b, a)
                case "^":
                    a = self.functions.deg(a, b)
                case "!^":
                    a = self.functions.deg(b, a)

            print("\nyour current result = ", a)
            self.wr_log(a, b, act, a_old)

            


