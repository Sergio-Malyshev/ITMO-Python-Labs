from random import randint
from time import perf_counter
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


def task_1():
    array1 = [randint(0, 99) for i in range(10 ** 6)]
    array2 = [randint(0, 99) for i in range(10 ** 6)]
    np_array1 = np.array(array1)
    np_array2 = np.array(array2)

    tstart1 = perf_counter()
    for i in range(10 ** 6):
        array1[i] *= array2[i]
    t1 = perf_counter() - tstart1

    tstart2 = perf_counter()
    np.multiply(np_array1, np_array2)
    t2 = perf_counter() - tstart2
    print(f"Время перемножения обычных списков: {t1}")
    print(f"Время перемножения NumPy массивов: {t2}")
    print(f"Разница во времени: {t1 - t2}")


def histogram1():
    a = np.genfromtxt('data2.csv', delimiter=',', skip_header=1)[:, 3]
    column = a[np.isfinite(a)]
    fig = plt.figure(figsize=(6, 4))
    ox = fig.add_subplot()
    ox.set_title('Гистограмма')
    ox.set_xlabel('Интерваллы')
    ox.set_ylabel('кол-во значений, попавших в интервалы')
    ox.hist(column, 16)
    ox.grid()


def histogram2():
    a = np.genfromtxt('data2.csv', delimiter=',', skip_header=1)[:, 3]
    column = a[np.isfinite(a)]
    fig = plt.figure(figsize=(6, 4))
    b = fig.add_subplot()
    b.set_title('Нормализированная гистограмма')
    b.hist(column, 16, density=True)
    b.set_xlabel('Интервалы')
    b.set_ylabel('Вероятность')
    b.grid()
    plt.show()
    print(f'среднеквадратичное отклонение: {np.std(column)}')


def graph3d():
    x = np.linspace(-3 * np.pi, 3 * np.pi)
    y = np.cos(x)
    z = np.array(x / np.sin(x))
    fig = plt.figure()
    graph = fig.add_subplot(111, projection='3d')
    graph.set_xlabel('X')
    graph.set_ylabel('Y')
    graph.set_zlabel('Z')
    graph.set_title('3d Graph')
    graph.plot(x, y, z, marker='x', c='green')
    plt.show()


def animation():
    fig, ax = plt.subplots()

    x = np.arange(0, 2 * np.pi, 0.1)
    line, = ax.plot(x, np.sin(x))

    def update(frame):
        line.set_ydata(np.sin(x + frame))
        return line,

    ani = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 50), blit=True)
    #ani.save('sin.gif', writer='pillow')
    ani = plt.show()


task_1()
histogram1()
histogram2()
graph3d()
animation()