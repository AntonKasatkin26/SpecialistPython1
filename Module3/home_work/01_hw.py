# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here
new_names = ''
i=1
for name in names:
    if i != len(names):
        new_names = new_names + name + ", "
    else:
        new_names = new_names + name
    i+=1
print(new_names)

# Пример вывода:
# Иван, Ирина, Вячеслав, Василий, Петр
