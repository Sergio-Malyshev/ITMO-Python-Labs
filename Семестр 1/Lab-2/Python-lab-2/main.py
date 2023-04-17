import csv


def esc(code):
    return f'\u001b[{code}m'


WHITE = esc(47)
RED = esc(41)
YELLOW = esc(43)
GREEN = esc(42)
END = esc(0)


def flag_benin():
    for i in range(8):
        if i < 4:
            print(f'{GREEN}{" " * 14}{YELLOW}{" " * 21}{END}')
        if i > 3:
            print(f'{GREEN}{" " * 14}{RED}{" " * 21}{END}')


def symbol(repeat):  # ячейка - 3, узор - 3*16*2
    for i in range(1, 17):
        if i == 1 or i == 17:
            line = f'{WHITE}{" " * 3 * 7}{GREEN}{" " * 3}{WHITE}{" " * 3 * 7}{END}'
            print(f'{line * repeat * 2}{END}')
            continue
        if i == 2 or i == 15:
            line = f'{WHITE}{" " * 3 * 6}{GREEN}{" " * 3 * 3}{WHITE}{" " * 3 * 6}{END}'
            print(f'{line * repeat * 2}{END}')
            continue
        if i == 3 or i == 14:
            line = f'{WHITE}{" " * 3 * 5}{GREEN}{" " * 3 * 5}{WHITE}{" " * 3 * 5}{END}'
            print(f'{line * repeat * 2}{END}')
            continue
        if i == 4 or i == 13:
            line = f'{WHITE}{" " * 3 * 4}{GREEN}{" " * 3 * 7}{WHITE}{" " * 3 * 4}{END}'
            print(f'{line * repeat * 2}{END}')
            continue
        if i == 5 or i == 12:
            line = f'{WHITE}{" " * 3 * 3}{GREEN}{" " * 3 * 9}{WHITE}{" " * 3 * 3}{END}'
            print(f'{line * repeat * 2}{END}')
            continue
        if i == 6 or i == 11:
            line = f'{WHITE}{" " * 3 * 2}{GREEN}{" " * 3 * 11}{WHITE}{" " * 3 * 2}{END}'
            print(f'{line * repeat * 2}{END}')
            continue
        if i == 7 or i == 10:
            line = f'{WHITE}{" " * 3}{GREEN}{" " * 3 * 13}{WHITE}{" " * 3}{END}'
            print(f'{line * repeat * 2}{END}')
            continue
        if i == 8 or i == 9:
            line = f'{GREEN}{" " * 3 * 15}{END}'
            print(f'{line * repeat * 2}{END}')
            continue


def array_init(array_in, st):
    for i in range(10):
        for j in range(10):
            if j == 0:
                array_in[i][j] = round(st * (8 - i) + st, 1)
            if i == 9:
                array_in[i][j] = round(j, 1)
    return array_in


def array_fill(array_fi, res, st):
    for i in range(9):
        for k in range(10):
            if abs(array_fi[i][0] - res[9 - k]) < st:
                for j in range(9):
                    if 8 - j == k:
                        array_fi[i][j + 1] = 1
    return array_fi


def print_plot(plot):
    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += WHITE + str(plot[i][j])
            if plot[i][j] == 0:
                line += '  '
            elif plot[i][j] == 1:
                line += RED + '  ' + WHITE
        line += END
        print(line)
    print(WHITE + '0   1 2 3 4 5 6 7 8 9' + END, "\n")


file = open('books.csv')
count = 0
price_check = 0
table = list(csv.reader(file, delimiter=';'))
for i, row in enumerate(table):
    if i == 0:
        continue
    price = row[7]
    if float(price) <= 150:
        price_check += 1
    count += 1

flag_benin()
r = input('Колличество повторений узора: ')
symbol(int(r))

array_plot = [[0 for col in range(10)] for row in range(10)]
result = [0 for i in range(10)]

print()
for i in range(10):
    result[i] = i + 1

step = round(abs((result[9] - result[0])) / 9, 1)

array_init(array_plot, step)
array_fill(array_plot, result, step)
print_plot(array_plot)

print(f'\n{GREEN}{" " * 3}{END}Книги до 150р', f'{YELLOW}{" " * 3}{END}Остальные книги\n')
for i in range(11):
    step = 10 * (10 - i)
    step_str = str(step).rjust(3, ' ')
    top1 = top2 = WHITE
    if (price_check / count) * 100 >= step:
        top1 = GREEN
    if ((count - price_check) / count) * 100 >= step:
        top2 = YELLOW
    print(f'{WHITE}{step_str}{top1}{" "}{WHITE}{" "}{top2}{" "}{END}')