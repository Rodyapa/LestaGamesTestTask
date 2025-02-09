# Вопрос 3
import random


def quicksort(arr):
    # Если массив содержит один элемент или пуст, он уже отсортирован
    # возвращаем этот же массив
    if len(arr) <= 1:
        return arr

    # Выбираем опорный элемент (в данном случае случайный)
    pivot = arr[random.randint(0, len(arr) - 1)]

    # Разделяем массив на элементы меньшие, равные и большие опорного
    less_than_pivot = [x for x in arr if x < pivot]
    equal_to_pivot = [x for x in arr if x == pivot]
    greater_than_pivot = [x for x in arr if x > pivot]

    # Рекурсивно применяем сортировку к меньшей и большей части массива
    return (quicksort(less_than_pivot)
            + equal_to_pivot
            + quicksort(greater_than_pivot))

# Пример использования
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quicksort(arr)
print(f"Отсортированный массив: {sorted_arr}")

# Плюсы:
# Время работы на среднем наборе данных — O(n log n),
# но в худшем случае (например, если массив уже отсортирован или
# состоит из одинаковых элементов) — O(n²).
# Однако при хорошем выборе опорного элемента,
# быстрота алгоритма на случайных данных обычно высока.
# Опять же. В среднем время работы алгоритма — O(n log n),
# что является наилучшим временем для алгоритмов сортировки.
#
# Объяснение эффективности:
#
# Сложность O(n log n): Ожидаемая сложность для случайного массива.
# Разделение массива на части уменьшает количество элементов,
# с которыми нужно работать.
# Реализация на основе случайного опорного элемента:
# Это помогает избежать худших сценариев
# (например, если массив уже отсортирован)
# и обеспечивает среднюю сложность O(n log n).
# Использование списковых включений: Это делает код компактным
# и эффективным с точки зрения синтаксиса

# В целом, для конкретных ситаций с конкретным возможным набором данных
# Можно написать более эффективный алгоритм.
# Можно использовать sorted функции, которая воплащает TimSort, гарантирующий
# время выполнение O(nlogn), но у TimSort тоже есть краевые случаи,
# когда TimSort будет потреблять больше памяти при сортировке больших массивов.
