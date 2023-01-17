import requests

r = requests.get("https://akabab.github.io/superhero-api/api/all.json")
superheroes = r.json()


def find_supers_index(iterable, key, value):
    for index, dict_ in enumerate(iterable):
        if key in dict_ and dict_[key] == value:
            return index


def compair_heroes():
    heroes = {}
    active_state = True
    while active_state is True:
        name = input('Введите имя героя: '
                     '\nЧтобы сравните введите done ')
        if name == 'done':
            active_state = False
            print(f'Самый умный {max(heroes, key=heroes.get)}')
        if active_state is True:
            index_of_hero = find_supers_index(superheroes, 'name', name)
            intellect_of_hero = superheroes[index_of_hero]['powerstats']['intelligence']
            heroes[name] = intellect_of_hero


compair_heroes()
