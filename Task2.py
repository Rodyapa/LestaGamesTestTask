# Вопрос №2
from collections import deque
import timeit
import sys


# 1 Вариант
class CircularBufferList:
    '''
    Реализация циклического буффера с использованием списка.
    Используем список для сохранения элементов, используем индексы для
    отслеживания старых и новых элементов.
    '''
    def __init__(self, size):
        self.size = size
        self.buffer = []  # Список для хранения элементов
        self.head = 0  # Указатель на место для записи нового элемента
        self.tail = 0  # Указатель на первый элемент для извлечения

    def push(self, item):
        # Если буффер не заполен, добавляем элемент.
        if len(self.buffer) < self.size:
            self.buffer.append(item)
        # Если буфер переполнен, заменяем элемент на месте head
        else:
            self.buffer[self.head] = item
        # Двигаем указатель head по круг
        self.head = (self.head + 1) % self.size
        # Если буфер полон, сдвигаем указатель tail по кругу
        if len(self.buffer) == self.size:
            self.tail = (self.tail + 1) % self.size

    def pop(self):
        if len(self.buffer) == 0:
            # Исключение, если буфер пустой
            raise IndexError("pop from empty buffer")
        item = self.buffer[self.tail]  # Берем элемент по указателю tail
        # Двигаем указатель tail по кругу
        self.tail = (self.tail + 1) % self.size
        return item

    def __repr__(self):
        return f"CircularBufferList({self.buffer})"

#   Плюсы этой реализаци:
# Можно контроллировать процесс размещения элементов в буффере.
# Простота и нативность реализации.
#   Минусы этой реализации:
# Список Python не оптимизирован для быстрого удаления и добавления элементов
# в начале или в середине списка. Пайтон при удалении или добавлении элемента
# в середину или начало списка - сдвигает все последующие элементы в памяти,
# что занимает время. То есть если мы вставялем элемент в начало списка,
# эта операция выполняется за O(n), n - колличество элементов списка.
# за O(1) пайтон может обратиться к индексу или сделать
# вставку или удалении только в конце списка.
# При каждом добавлении элемента список будет автоматически расширяться,
# что может приводить к лишним перераспределениям памяти.


# 2 Вариант

class CircularBufferDeque:
    '''
    Реализация циклического буффера с использованием объекта deque из
    стандартной библиотеки Python.
    '''
    def __init__(self, size):
        self.size = size
        # Инициализация буфера с заданным размером,
        # используя deque с максимальной длиной
        self.buffer = deque(maxlen=size)

    def push(self, item):
        self.buffer.append(item)

    def pop(self):
        if not self.buffer:
            raise IndexError("pop from empty buffer")
        return self.buffer.popleft()

    def __repr__(self):
        return f"CircularBufferDeque({list(self.buffer)})"

#   Плюсы этой реализаци:
# Используется класс deque, который предоставляет оптимизированные методы
# добавления и удаления элементов с обоих концов. Все методы пвыолняются за
# O(1)
# deque автоматически удаляет элементы с начала, когда их становится больше
# указанного размера. Меньше кода.
#   Минусы этой реализации:
# Может быть использовано больше памяти по сравнению с списком.
# Вместо того чтобы хранить все элементы в одном непрерывном участке памяти
# (как это делает обычный список), deque использует несколько блоков памяти.
# Эти блоки связаны между собой и организуют кольцевую очередь,
# что позволяет эффективно добавлять и удалять элементы с обеих сторон.
# Каждый блок имеет накладные расходы,
# связанные с указателями на соседние блоки, что увеличивает общий объем памяти
# требуемый для хранения всех элементов.
# deque может заранее выделять больше памяти, чтобы предотвратить частые
# перераспределения памяти при добавлении новых элементов.
# Не такая гибкость: deque — это более специализированная структура данных,
# и если требуется специфическое поведение,
# оно может быть не так легко реализуемо, как с обычным списком.


# Тест для списка
def test_list_operations():
    list_buffer = CircularBufferList(size=10**5)
    for i in range(10**6):
        list_buffer.push(i)  # Добавление в конец списка
    for i in range(10**5):
        list_buffer.pop()  # Удаление из начала списка


# Тест для deque
def test_deque_operations():
    deque_buffer = CircularBufferDeque(size=10**5)
    for i in range(10**6):
        deque_buffer.push(i)  # Добавление в конец deque
    for i in range(10**5):
        deque_buffer.pop()  # Удаление из начала deque


# Измерение времени с использованием timeit
list_time = timeit.timeit(test_list_operations, number=1)
deque_time = timeit.timeit(test_deque_operations, number=1)

print(f"Время работы с list: {list_time:.4f} секунд")
print(f"Время работы с deque: {deque_time:.4f} секунд")

assert (list_time > deque_time) is True


list_buffer = CircularBufferList(size=10**5)
for i in range(10**5):
    list_buffer.push(i)
list_size = sys.getsizeof(list_buffer.buffer)

deque_buffer = CircularBufferDeque(size=10**5)
for i in range(10**5):
    deque_buffer.push(i)
deque_size = sys.getsizeof(deque_buffer.buffer)

print(f"Размер буффера в виде списка: {list_size / (1024 ** 2):.3f} MB")
print(f"Размер буффера в виде deque: {deque_size / (1024 ** 2):.3f} MB")

assert (deque_size > list_size) is True
