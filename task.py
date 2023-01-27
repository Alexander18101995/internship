def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    print(f"Факториал от числа {n} = {fact}")
factorial(int(input('Введите число: ')))


line = input("Введите строку: ")
substring = input("Введите подстроку: ")
print(line.count(substring))