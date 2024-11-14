list = [{'name':"Jon", 'mark':63}, 
         {'name':"Emma", 'mark':71},
         {'name':"Bob", 'mark':68},
         {'name':"Max", 'mark':85}]

while True:
    n_m = input("Select sorting: N — name, M — mark, 'ex' — to end the program: ")
    if n_m == "ex":
        exit(0)
    elif n_m == "N":
        for name in sorted(list, key = lambda elem : elem["name"]):
            print(f"Name — {name['name']} | Mark — {name['mark']}")
    elif n_m == "M":
        for name in sorted(list, key = lambda elem : elem["mark"]):
            print(f"Name — {name['name']} | Mark — {name['mark']}")
