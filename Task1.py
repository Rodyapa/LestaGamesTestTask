# Вопрос №1
import timeit
import random


def is_even_bitwise(value):
    '''
    Реализация функции с использованием побитового оператора &.

    В двоичной системе счисления четные числа заканчиваются на 0,
    а нечетные на 1.
    Если применить побитовую операцию AND к какому-либо числу и числу 1,
    то результат будет 0 для четных чисел и 1 для нечетных.
    '''
    return (value & 1) == 0

# Плюсы: побитовая операция быстее, чем деление.
# Минусы: Работает только с целыми числами. Может работать некорректно
# Если число представленно пользовательским классом с переопределенным
# методом __and__


assert is_even_bitwise(0) is True
assert is_even_bitwise(1) is False
assert is_even_bitwise(-1) is False
assert is_even_bitwise(2) is True
assert is_even_bitwise(-2) is True
assert is_even_bitwise(10) is True
assert is_even_bitwise(100) is True
assert is_even_bitwise(1000) is True
assert is_even_bitwise(-10) is True
assert is_even_bitwise(-100) is True
assert is_even_bitwise(-1000) is True


# Реализация с остатком
def is_even_mod(value):
    return value % 2 == 0
# Плюсы реализации через оператор остатка от деления:
# Более интуитивная реализация. Применима к float type.
# Минусы: Медленее чем побитовая операция.

# Тест проверяет, что побитовая операция быстрее чем операция нахождения
# остатка от деления.


# Колличество чисел для теста
N = 10**6

# Рандомные числа
values = [random.randint(-10**6, 10**6) for _ in range(N)]

mod_time = timeit.timeit(
    lambda: [is_even_mod(x) for x in values], number=1
)
bitwise_time = timeit.timeit(
    lambda: [is_even_bitwise(x) for x in values], number=1
)


print(f'Операция с нахождением остатка: {mod_time:.6f} секунд')
print(f'Операция с побитовым AND: {bitwise_time:.6f} секунд')
assert (mod_time > bitwise_time) is True
