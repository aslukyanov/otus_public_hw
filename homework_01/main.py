"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    #final_lst = list(map(lambda x : x ** 2, args))
    final_lst = [i ** 2 for i in args]
    return final_lst

#print(power_numbers(1, 2, 5, 7))

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(numbers) :
    final_lst =[]
    for i in numbers :
        count = 0
        for j in range(2, i, 1) :
            if i % j == 0 :
                count += 1
        if count == 0 :
            final_lst.append(i)
    return final_lst

#print(is_prime([1,2,3,4,5,7,9,8,22,21]))

def filter_numbers(numbers, condition):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    if condition == ODD :
        return list(filter(lambda x : True if x % 2 == 1 else False, numbers))
    if condition == EVEN :
        return list(filter(lambda x : True if x % 2 == 0 else False, numbers))
    if condition == PRIME :
        return is_prime(numbers)


#print(filter_numbers([1,2,3,4,5,6,7,8,9], ODD))
#print(filter_numbers([2,3,4,5,6,7,8,9,10], EVEN))
#print(filter_numbers([3,4,5,6,7,8,9,11], PRIME))





