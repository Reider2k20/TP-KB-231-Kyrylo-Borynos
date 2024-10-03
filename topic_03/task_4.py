def sort_pos(list, item):
    insert_pos = 0
    for elem in list:
        if item > elem:
            insert_pos += 1
        else:
            break
    return insert_pos

names_list = ["Andrew", "Bob", "Emma", "Michael", "Tomas" ]

print(f"List of names: {names_list}")

name = input("Enter a new name to get a position to insert it: ")
pos = sort_pos(names_list, name)

if pos == 0:
    print("This name will be inserted first")
elif pos == len(names_list):
    print("This name will be inserted last")
else:
    print(f"This name will be inserted between {names_list[pos - 1]} and {names_list[pos]}.")