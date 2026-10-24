x = int(input("Введите x: "))
y = int(input("Введите y: "))
while type(x) != float:
    try:
        x = float(x)
    except ValueError:
        print("Неправильно ввели: ")
        x = int(input("Введите x: "))
while type(y) != float:
    try:
        y = float(y)
    except ValueError:
        print("Ввудите y: ")
if x > 0 and y < 0:
    print("Истинна")
else:
    print("Ложь")
