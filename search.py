# На вход программе подается натуральное число nn, затем nn строк, затем еще одна строка — поисковый запрос. Напишите
# программу, которая выводит все введенные строки, в которых встречается поисковый запрос.
#
# *** Формат входных данных ***
# На вход программе подаются натуральное число nn — количество строк, затем сами строки в
# указанном количестве, затем один поисковый запрос.
#
# *** Формат выходных данных ***
# Программа должна вывести все введенные строки, в которых встречается поисковый запрос.
#
# *** Примечание. *** Поиск не должен быть чувствителен к регистру символов.

# задать количество вводимых строк
n = int(input())

# организовать ввод строк
strings = []
for _ in range(n):
    strings.append(input())

# задать поисковый запрос нечувствительный к регистру
search = input()

# вывод результатов поиска
result = []
for i in range(n):
    if search.lower() in strings[i].lower():
        result.append(strings[i])
print(*result, sep='\n')
