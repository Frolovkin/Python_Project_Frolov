# Даны два целых числа A и B(A<B).
# Вывести в порядке убывания все целые числа, расположенные между A и B (не вкл числа A и B),
# а также количество N этих чисел.
while True:
    try:
        a = int(input("Введите число A: "))
        break
    except ValueError:
        print("Введите правильное число")
while True:
    try:
        b = int(input("Ввндите число B: "))
        if a < b:
            break
        else:
            print:("Число A должно быть меньше числа B.")
    except ValueError:
        print("Введите правильно число")
n = 0
while b - a > 1:
    b -= 1
    print(b)
    n += 1
print("Количество чисел:", n)