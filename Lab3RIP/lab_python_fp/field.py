def field(items, *args):
    assert len(args) > 0
    i = 0
    j = 0
    d1 = {}
    for i in range(len(items)):
        for j in range (len(args)):
            d1[args[j]] = items[i][args[j]]
        print(d1)    

def main():
    print('Задание 1:')
    goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    print('Пример 1:')
    field(goods, 'title')
    print('Пример 2:')
    field(goods, 'title', 'price')


if __name__ == "__main__":
    main()