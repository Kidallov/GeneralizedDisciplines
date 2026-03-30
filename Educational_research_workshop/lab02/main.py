import numpy as np
import random

# Пузырьковая сортировка
def bubble_sort(arr):

    # Будет считать количесвто проходов
    for i in range(len(arr)): 

        # Создаем уже внутренний проход
        for j in range(0, len(arr) - i - 1):
            
            # Проверяем, что элемент не выходит за пределы массива
            if j + 1 < len(arr):
                
                # Сравниваем и переставляем
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

# Быстрая сортировка
def quick_sort(arr):

    # Проверка на размер
    if len(arr) <= 1: 
        return arr

    # Создаем пивот, случайно выбранное значение, с которым будем сравнивать
    pivot = random.choice(arr)
    
    # Создаем массивы, куда будем расклыдвать элементы относительно pivot
    right, left, middle = [], [], []
    
    for i in range(len(arr)):

        if pivot < arr[i]:
            right.append(arr[i])
        
        elif pivot > arr[i]:
            left.append(arr[i])

        else:
            middle.append(arr[i])

    # Объединяем наши списки
    return quick_sort(left) + middle + quick_sort(right) 
