def update_test(dictionary):
    new_dictionary = {'fourth': 44, 'fifth': 55}
    dictionary.update(new_dictionary)
    print("Функція update() додає або оновлює пари ключ-значення в словнику: ", dictionary)

def del_test(dictionary):
    del dictionary['second']
    print("Функція del() видаляє елемент з заданим ключем 'second': ", dictionary)

def clear_test(dictionary):
    dictionary.clear()
    print("Функція clear() очищає словник: ", dictionary)

def keys_test(dictionary):
    keys = dictionary.keys()
    print("Функція keys() повертає всі ключі зі словника: ", keys)

def values_test(dictionary):
    values = dictionary.values()
    print("Функція values() повертає всі значення зі словника: ", values)

def items_test(dictionary):
    items = dictionary.items()
    print("Функція items() повертає всі пари ключ-значення у вигляді кортежів: ", items)

dictionary1 = {'first': 11, 'second': 22, 'third': 33}

# Для виклику функцій використовується копія словника, щоб не змінювати сам словник
print("Оригінальний словник: ", dictionary1)
update_test(dictionary1.copy())
del_test(dictionary1.copy())
clear_test(dictionary1.copy())
keys_test(dictionary1.copy())
values_test(dictionary1.copy())
items_test(dictionary1.copy())