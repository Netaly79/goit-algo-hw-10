import matplotlib.pyplot as plt
import numpy as np
import random
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2 + 3 * x - 3

def draw():
    a = 0  # Нижня межа
    b = 3  # Верхня межа
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()

def monte_carlo(func, a, b, num_samples):
    count_under_curve = 0

    for _ in range(num_samples):
        x = random.uniform(a, b)
        y = random.uniform(0, max(func(a), func(b)))

        if y <= func(x):
            count_under_curve += 1

    area_rectangle = (b - a) * max(func(a), func(b))
    area_under_curve = (count_under_curve / num_samples) * area_rectangle

    return area_under_curve

def main():
    draw()
    monte_carlo_result = monte_carlo(f, 0, 3, 1000)
    print("\nCalculated using Monte Carlo with 1 000:   ", monte_carlo_result)
    monte_carlo_result = monte_carlo(f, 0, 3, 10000)
    print("Calculated using Monte Carlo with 10 000:  ", monte_carlo_result)
    result, error = spi.quad(f, 0, 3)
    print("Math calculation: ", result, "\n")

if __name__ == "__main__":
    main()