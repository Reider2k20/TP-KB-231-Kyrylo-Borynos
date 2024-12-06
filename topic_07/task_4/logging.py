import os
from datetime import datetime


class Logger:
    def __init__(self, file_name="Calc_Log.txt"):
        self.file_path = os.path.join(os.path.dirname(__file__), file_name)

    def log(self, a, b, act, a_old):
        log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if not act:
            pass
        elif act in ["!-", "!/","!^"]:
            with open(self.file_path, "a") as file:
                file.write(f"{log_time} | {b} {act[1]} {a_old} = {a}\n")
        else:
            with open(self.file_path, "a") as file:
                file.write(f"{log_time} | {a_old} {act} {b} = {a}\n")
