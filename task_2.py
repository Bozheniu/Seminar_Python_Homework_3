"""Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]"""""

list = list(map(int, input("Введите числа через пробел:\n").split()))
new_list = []

for i in range(len(list)//2):
    count1 = list[i] * list[len(list) - i - 1]
    result = new_list.append(count1)

print(new_list)