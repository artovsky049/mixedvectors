import numpy as np
import time

print("ПО для вычисления смешанного произведения векторов. (C) Andron Artemev 2023")
time.sleep(0.5)

def mixed_product(v1, v2, v3):
    return np.dot(v1, np.cross(v2, v3))

def input_vector():
    return np.array(list(map(int, input("Введите координаты вектора через пробел: ").split())))

v1 = input_vector()
v2 = input_vector()
v3 = input_vector()

print("Смешанное произведение векторов: ", mixed_product(v1, v2, v3))