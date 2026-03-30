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


def quick_sort(arr):

    if len(arr) <= 1: 
        return arr

    pivot = random.choice(arr)
        
    left = [i for i in arr if i < pivot]
    middle = [i for i in arr if i == pivot]
    right = [i for i in arr if i > pivot]

    return quick_sort(left) + middle + quick_sort(right)
    


# Случайный массив длиной в 10 ^ 8
#arr = np.random.rand(10**8)
arr = [3,14,1,7,9,8,11,6,4,2]

print(bubble_sort(arr))
print(quick_sort(arr))