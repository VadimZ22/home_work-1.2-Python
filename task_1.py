# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#      *Пример:*
#     - 6782 -> 23
#     - 0.56 -> 11

def Sum_Digits(num):
    sum = 0
    count = 0
    while num >= 1:
        sum += num % 10
        num = num // 10
    return sum

def Sum_Digits_Str(number):
    number = str(number)
    number.split()
    sum = 0
    for i in number:
        if i != '.':
            sum += int(i)
    return sum




number = float(input("enter any number: "))
num1 = int(number // 1)
num2 = number % 1
for i in range(len(str(number).split('.')[1])):
    num2 *= 10
num2 = int(num2//1)


print(f'Вывод через float: {Sum_Digits(num1) + Sum_Digits(num2)}')
print(f'Вывод через string: {Sum_Digits_Str(number)}')















