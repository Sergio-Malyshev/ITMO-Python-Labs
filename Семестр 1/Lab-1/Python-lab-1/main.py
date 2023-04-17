import csv
from random import random

count = 0  # счетчик кол-ва записей
count_in_file = 0
big_name_count = 0  # название >30
name = 0  # название книги
file = open("books.csv", "r")
output_file = open("output.txt", "w")
table = list(csv.reader(file, delimiter=';'))

for i, row in enumerate(table):
    name = row[1]

    if i == 0:
        continue

    if len(name) > 30:
        big_name_count += 1
    count += 1

print("Кол-во записей в файле -", count, "|task 1")
print("Кол-во названий длинее 30 символов -", big_name_count, "|task 2")

author_name = input("Введите фио автора: ").lower()

for i, row in enumerate(table):

    if i == 0:
        continue

    date = row[6]
    year = int(date[6:10])
    author = row[3]
    if (year == 2015 or year == 2018) and author.lower() == author_name:
        print(row[4], ".", row[1], "-", row[6][6:10])

for i, row in enumerate(table):
    if i == 0:
        continue
    author = row[3]
    name = row[1]
    date = row[6]
    if random() < 0.2 and count_in_file < 20:
        count_in_file += 1
        print(f"{i} {row[1]}. {row[3]}- {row[6][6:10]}", file=output_file)
file.close()
output_file.close()