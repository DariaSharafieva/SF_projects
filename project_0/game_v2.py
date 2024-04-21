"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def binary_search(number: int = 1) -> int:
    """Угадываем число по алгоритму бинарного поиска

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    low = 0
    high = 1000
    
    while low <= high:
        count += 1
        mid = (low+high) / 2
        if mid == number:
            break # Выход из цикла, если угадали
        if mid > number:
            high = mid-1 
        else:
            low = mid+1
            
    return count


def score_game(binary_search) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(binary_search(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(binary_search)
