def extend_test(list):
    new_list = [14, 12]
    list.extend(new_list)
    print("Функція extend() додає до списку елемнети іншого списку: ", list)

def append_test(list):
    list.append(15)
    print("Функція append() додає елемнет в кінець списку: ", list)

def insert_test(list):
    list.insert(3, 23)
    print("Функція insert() вставляє елемент 23 на позицію з індексом 3: ", list) # Все, що лівіше у списку (0-2) не змінить свій індекс, а все, що правіше, включаючи 3 (3-...) збільшить його на 1

def remove_test(list):
    list.remove(4)
    print("Функція remove() видалить перший елемент із значенням 4: ", list)

def clear_test(list):
    list.clear()
    print("Функція clear() очищає список: ", list)

def sort_test(list):
    list.sort()
    print("Функція sort() сортує список: ", list)

def reverse_test(list):
    list.reverse()
    print("Функція reverse() змінює порядок елементів на зворотній: ", list)

def copy_test(list):
    copy_list = list.copy()
    print("Функція copy() створює копію списку: ", copy_list)

list1 = [1, 4, 6, 2, 3, 10, 8, 4]

# Для виклику функцій використовується копія списку, щоб не змінювати сам список
print("Оригінальний список: ", list1)
extend_test(list1.copy())
append_test(list1.copy())
insert_test(list1.copy())
remove_test(list1.copy())
clear_test(list1.copy())
sort_test(list1.copy())
reverse_test(list1.copy())
copy_test(list1)
