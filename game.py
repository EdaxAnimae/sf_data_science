import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    left = 0
    rigth = 100
    while True:
        predict_number = round((left+rigth)/2) # предполагаемое число
        count += 1
        if number == predict_number:
            break # выход из цикла, если угадали
        elif number > predict_number:
            left = predict_number
        else:
            rigth = predict_number
    return(count)

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

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

score_game(random_predict)