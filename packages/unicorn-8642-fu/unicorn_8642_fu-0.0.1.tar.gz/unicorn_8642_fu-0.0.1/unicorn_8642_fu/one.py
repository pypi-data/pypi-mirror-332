a = float(input("Введите a: "))
b = float(input("Введите b: "))

if a == 0:
    print("Решений нет" if b != 0 else "Бесконечно много решений")
else:
    x = -b / a
    print(f"Решение: x = {x}")
