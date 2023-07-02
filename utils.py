from random import sample


def get_word():
    """
    Получаем список слов из файла
    """
    words = []
    with open('words.txt', encoding='utf-8') as file:
        for line in file:
            words.append(line.rstrip('\n'))
    return words


def get_shuffle_word(word):
    """
    Перемешивает слово
    """
    return ''.join(sample(word, len(word)))


def get_user_history(user_name):
    """
    История пользователя
    """
    history = []
    with open('history.txt', encoding='utf-8') as file:
        for users in file:
            if user_name in users:
                history.append(users.rstrip().split(' '))
    record = (max(history))
    print(f'Всего игр сыграно: {len(history)}\nМаксимальный рекорд: {record[1]}')


def make_user_record(user_name, user_score):
    """
    Делаем запись результата пользователя
    """
    with open('history.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{user_name.strip().capitalize()} {user_score}')
