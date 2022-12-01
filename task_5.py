# Реализуйте алгоритм генерации случайного числа.(Не используя библиотеки связанные с рандомом)

import datetime

def Random_Num():
    time = datetime.datetime.now()
    num1 = time.hour
    if time.hour == 0: num1 = 1
    num2 = time.minute
    num3 = time.second
    result = num1 * num2 * num3
    return result

print(Random_Num())