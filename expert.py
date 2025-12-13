import numpy as np
import matplotlib.pyplot as plt

# Параметры
r_min = 0
r_max = 27 / (2*(7*7**0.5 - 10))
num_r = 50000  # количество значений r
x0 = 0.5     # начальная точка
n_iter = 1000  # общее число итераций
n_save = 50    # сколько последних точек сохранять

# Создаём массив значений r
r_values = np.linspace(r_min, r_max, num_r)

# Списки для хранения точек графика
r_plot = []
x_plot = []

# Основной цикл по r
for r in r_values:
    x = x0  # сбросим x к начальному значению
    
    # делаем n_iter итераций, чтобы "забыть" начальное условие
    for _ in range(n_iter):
        x = r * x * (1 - x)*(3 - x)
    
    # сохраняем последние n_save значений
    for _ in range(n_save):
        x = r * x * (1 - x)
        r_plot.append(r)
        x_plot.append(x)

# Шаг 5: строим график
plt.figure(figsize=(10, 6))
plt.scatter(r_plot, x_plot, s=0.1, color='black', alpha=0.5)
plt.title('Бифуркационная диаграмма g(x) отображения')
plt.xlabel('$r$')
plt.ylabel('$x$')
plt.xlim(r_min, r_max)
plt.ylim(0, 1)
plt.grid(True, alpha=0.3)
plt.show()