from utils import get_word, get_shuffle_word, get_user_history, make_user_record

SCORE = 10

# счетчик баллов пользователя
user_score = 0

# знакомство с пользователем
user_name = input('Напиши как тебя величать:\n').strip().capitalize()

# цикл для исключения строки без символов
while True:
    if user_name != '' and user_name != ' ':
        break
    else:
        user_name = input('Анонимов не любим, укажи как тебя записать:\n')

# цикл вопросов
for word in get_word():
    user_answers = input(f'Угадай слово: {get_shuffle_word(word)}\n')
    if user_answers.strip().lower() == word:
        user_score += SCORE
        print(f'Верно, это {word}! Вы получаете {SCORE} баллов! =)')
    else:
        print(f'Потрачено! =( Верный ответ - {word}.')

# вывод результатов и статистики
make_user_record(user_name, user_score)
print(f'{user_name}, ты заработал(а) {user_score} баллов.')
get_user_history(user_name)
