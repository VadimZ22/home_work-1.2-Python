# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#      *Пример:*
#      - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


n = int(input("Inter a number: "))
product = 1
kit = []
for i in range(1, n + 1):
    product *= i
    kit.append(product)
print(kit)