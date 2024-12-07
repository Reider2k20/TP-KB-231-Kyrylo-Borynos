class Student:
    def __init__(self, name, phone, group, debt):
        self.name = name
        self.phone = phone
        self.group = group
        self.debt = debt

    def __str__(self):
        return f"Student name is {self.name},  Phone is {self.phone},  Group is {self.group},  debt is {self.debt} UAH"