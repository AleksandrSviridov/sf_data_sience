import numpy as np

def random_predict(number: int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    number = np.random.randint(1, 101)
    min_number = 0
    max_number = 100
    count = 0
    
    while True:
        count += 1
        predict_number = round((min_number + max_number)/2) # приминяем бинарный поиск числа
        if number == predict_number:
            break
        elif number > predict_number:
            min_number = predict_number
        elif number < predict_number:
            max_number = predict_number
        
    return(count)
    
print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) 

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


if __name__ == '__main__':
    score_game(random_predict)