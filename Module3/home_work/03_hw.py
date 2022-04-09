# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
import random
list_elements = []
counter = 0
amount_elements = int(input("введите количество элементов списка: "))
while counter < amount_elements:
    list_elements.append(random.randint(-100, 100))
    counter += 1
print("Сгенерированные элементы списка: ", list_elements)

summa_elements = 0
for element in list_elements:
    if element > 0 and element % 2 == 0:
        summa_elements += element
    else:
        summa_elements = 0

print("Cумма элементов списка кратных двум = ", summa_elements)
