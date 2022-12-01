# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.


n = int(input("Enter a number: "))
elements = [i for i in range(-n, n+1)]
# for i in range(-n, n+1):
#     elements.append(i)
print(elements)
list_position = []
with open('file.txt') as data:
    list_position = [int(i) for i in data]
    # for i in data:
    #     list_position.append(int(i))
print(list_position)
product = 1
for i in list_position:
    product *= elements[i]
print(product)



