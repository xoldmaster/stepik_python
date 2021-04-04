# На вход программе подается натуральное число n, а затем n строк. Напишите программу, которая выводит только
# уникальные строки, в том же порядке, в котором они были введены.
#
# *** Формат входных данных ***
# На вход программе подаются натуральное число n, а затем n строк, каждая на отдельной строке.
#
# *** Формат выходных данных ***
# Программа должна вывести текст в соответствии с условием задачи.
#
# *** Примечание. *** Считайте, что все строки состоят из строчных символов.

n = int(input())
words = []
new_words = []
duplicates_indexes = []

for _ in range(n):
    words.append(input())

for char in range(n):
    for char_d in range(char + 1, n):
        if words[char_d] == words[char]:
            duplicates_indexes.append(char_d)

for i in range(n):
    if i not in duplicates_indexes:
        new_words.append(words[i])

print(new_words)
