import numpy as np
import math
def compute_factorial(n):
    # Вычисление факториала
    return math.factorial(n)
def generate_matrix(x):
    # Генерация матрицы размера x
    return np.random.rand(x, x)
def compute_series_sum(matrix, t):
    sum_result = 0.0
    n = 0
    first_term_sign = np.random.choice([-1, 1])
    current_term = first_term_sign * np.abs(np.linalg.det(matrix[3*n:3*(n+1), 3*n:3*(n+1)])) / compute_factorial(3*n)
    # Первое слагаемое

    while abs(current_term) >= 10**(-t):
        sum_result += current_term
        n += 1
        current_term = (-1)**n * np.abs(np.linalg.det(matrix[3*n:3*(n+1), 3*n:3*(n+1)])) / compute_factorial(3*n)
        # Сумма слагаемых
    return round(sum_result, t)

# Вводим размер матрицы x, ранг матрицы k и точность t
x = int(input("Введите размер матрицы x: "))
k = int(input("Введите ранг матрицы k: "))
t = int(input("Введите точность t: "))

# Генерируем матрицу размера x
random_matrix = generate_matrix(x)

# Вычисляем сумму ряда с заданной точностью
result = compute_series_sum(random_matrix, t)

print("Сумма знакопеременного ряда:", result)
