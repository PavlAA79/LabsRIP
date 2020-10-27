
def print_result(func_to_decorate):
    def decorated_func(*args):
        print(func_to_decorate.__name__)
        obj = func_to_decorate(*args)
        if isinstance(obj, dict):
            for i in obj.items():
                print('{} = {}'.format(i[0], i[1]))
            return obj
        elif isinstance(obj, list):
             for i in range(len(obj)):
                print('{}'.format(obj[i]))
             return obj
        else:
            print(obj)
            return obj

    return decorated_func


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]

def main():
    print('Задание 5:')
    test_1()
    test_2()
    test_3()
    test_4()

if __name__ == "__main__":
    main()