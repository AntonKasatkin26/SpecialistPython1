# По данному числу n закончите фразу «На лугу пасется...» одним из возможных продолжений:
# «n коров», «n корова», «n коровы», правильно склоняя слово «корова».
# Формат входных данных
# Дано целое положительное число n
# Формат выходных данных
# Программа должна вывести введенное число n и одно из слов (на латинице):
# коров, корова или коровы
# Например, 1 корова, 2 коровы, 5 коров, 125 коров.

# TODO: your code here
n = int(input("Введите кол-во коров: "))
if 11 <= n % 100 <= 20:
#    print(n, " коров")
#elif n % 10 == 1:
#    print(n, " корова")
#elif 1 < n % 10 < 5:
#    print(n, " коровы")
#else:
