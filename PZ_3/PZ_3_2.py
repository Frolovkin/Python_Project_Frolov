a = int(input("Вудите превое число: "))
b = int(input("Введите второе чило: "))
c = int(input("Введите третье число: "))
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели: ")
        a = input("Введите первое число: ")
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели: ")
        b = input("Введите второе число: ")
while type(c) != int:
    try:
        c = int(c)
    except ValueError:
        print("Неправильно ввели: ")
        c = input("Введите третье число: ")