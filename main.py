"""Задание №1"""
with open('text.txt', 'r') as f:
    # print(f.read())
    cook_book = {}
    for i, line in enumerate(f, 1):
        name_dish = line.strip()
        cook_book[name_dish] = []
        a = int(f.readline().strip())
        # print(a)
        for j in range(a):
            dict_1 = {}
            list_1 = f.readline().strip().split('|')
            # print(list_1)
            cook_book[name_dish].append({'ingredient_name': list_1[0], 'quantity': list_1[1], 'measure': list_1[2]})
            # (cook_book[name_dish])
        f.readline()
    # pprint.pprint(cook_book)



def get_shop_list_by_dishes(dishes, person_count):
    dict_ing = {}
    for i in dishes:
        for j in range(len(cook_book[i])):

            if i in cook_book:

                if cook_book[i][j]['ingredient_name'] not in dict_ing:

                    dict_ing[cook_book[i][j]['ingredient_name']] = {'measure': cook_book[i][j]['measure'],
                                                                    'quantity': int(
                                                                        cook_book[i][j]['quantity']) * person_count}

                else:
                    dict_ing[cook_book[i][j]['ingredient_name']]['quantity'] += int(
                        cook_book[i][j]['quantity']) * person_count
                    # print('10',int(cook_book[i][j]['quantity']))
                    # c = dict_ing[cook_book[i][j]['ingredient_name']]
                    # print(dict_ing[[c]['quantity']])
                    # dict_ing[cook_book[i][j]['ingredient_name']['quantity']] += int(cook_book[i][j]['quantity'])
    print(dict_ing, 'sort_dicts=False')


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Омлет'], 2)

