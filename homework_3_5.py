# Задание 5
import random

NOUNS = ["автомобиль", "лес", "огонь", "город", "дом"]
ADVERBS = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
ADJECTIVES = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# Создаем списки как константы

def get_jokes(n, repeat = False):


    jokes = []
    if not repeat:
        nouns_copy = NOUNS.copy()
        random.shuffle(nouns_copy)
        adverbs_copy = ADVERBS.copy()
        random.shuffle(adverbs_copy)
        adjectives_copy = ADJECTIVES.copy()
        random.shuffle(adjectives_copy)
        # создаем копии списков
        for num, (noun, adverb, adjective) in enumerate(zip(nouns_copy, adverbs_copy, adjectives_copy)):
            jokes.append(f'{noun} {adverb} {adjective}')
            if num == n:
                break
    else:
        for _ in range(n):
            jokes.append(f'{random.choice(NOUNS)} {random.choice(ADVERBS)} {random.choice(ADJECTIVES)}')
    return jokes

print(get_jokes(n=3))
