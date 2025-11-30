import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
import math

# Лестница Ламарея
def ladder_lamerey(r, x0, steps):
    '''
    Получает на вход значение r, x0 и кол-во ступенек
    Строит лестницу Ламерея
    '''
    '''Строим логистическое отображение'''
    def f(x):
        return r * x * (1 - x)

    '''Кол-во ступенек соответствует количеству элементов последовательности
    Создаём список этим элементов по порядку'''
    x_vals = [x0]
    for i in range(steps):
        x_vals.append(f(x_vals[-1]))

    '''Создаём окно и координатную плоскость размера 6на6'''
    fig, ax = plt.subplots(figsize=(6, 6))

    '''Каждому значению x ставим с соответствие f(x) = y'''
    x_plot = np.linspace(0, 1, 400)
    y_plot = f(x_plot)

    '''Строим график прямой и график логистического отображения'''
    ax.plot(x_plot, y_plot, label='y = rx(1-x)')
    ax.plot(x_plot, x_plot, label='y = x')

    '''Построение лестницы по значениям последовательности'''
    for i in range(len(x_vals) - 1):
        ax.plot([x_vals[i], x_vals[i]], [x_vals[i], x_vals[i+1]]) #верт. шаг
        ax.plot([x_vals[i], x_vals[i+1]], [x_vals[i+1], x_vals[i+1]]) #горизонт. шаг

    '''Оформление графика и вывод'''
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title(f'Лестница Ламерея: r = {r}, x0 = {x0}')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    plt.show()

ladder_lamerey(2, 0.2, 500)