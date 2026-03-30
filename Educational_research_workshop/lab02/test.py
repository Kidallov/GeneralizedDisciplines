import time
import random
from main import bubble_sort, quick_sort

def benchmark():
    """Замеряет время выполнения сортировок"""
    
    sizes = [1000, 10000, 50000]
    
    print("\n" + "="*70)
    print(f"{'Размер':^10} | {'Пузырьковая сортировка':^25} | {'Быстрая сортировка':^25}")
    print("="*70)
    
    for size in sizes:
        # Генерируем случайный массив
        test_array = [random.randint(1, 100000) for _ in range(size)]
        
        # Замеряем пузырьковую сортировку
        arr_copy = test_array.copy()
        start = time.time()
        bubble_sort(arr_copy)
        bubble_time = time.time() - start
        
        # Замеряем быструю сортировку
        arr_copy = test_array.copy()
        start = time.time()
        quick_sort(arr_copy)
        quick_time = time.time() - start
        
        # Выводим результаты
        print(f"{size:^10} | {bubble_time:^25.6f} | {quick_time:^25.6f}")
    
    print("="*70)

if __name__ == "__main__":
    benchmark()