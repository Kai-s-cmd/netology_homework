from pprint import pprint

file_path = '/home/alex/Documents/pythonProject/netology/python/recipes.txt'
recipes = 'recipes.txt'


def make_cook_book(recipes):
    cook_book = {}

    with open(recipes, encoding='UTF-8') as file:
        for line in file:
            clean_string = line.strip()
            quantity_of_ingredients = int(file.readline())
            ingredients = []
            for i in range(quantity_of_ingredients):
                ingr = file.readline().split(' | ')
                dish_ingredients = {'ingredient_name': ingr[0].strip(),
                                    'quantity': int(ingr[1]),
                                    'measure': ingr[2].strip()}
                ingredients.append(dish_ingredients)
            cook_book[clean_string] = ingredients
            file.readline()
    return cook_book


pprint(make_cook_book(file_path), width=70)


def get_shop_list_by_dishes(dishes, persons):
    shop_list = {}
    for dish, ingredient in make_cook_book(recipes).items():
        if dish in dishes:
            for ingr in ingredient:
                half_dict = {'measure': list(ingr.values())[2],
                             'quantity': list(ingr.values())[1] * persons}
                shop_list[list(ingr.values())[0]] = half_dict
    return shop_list


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
