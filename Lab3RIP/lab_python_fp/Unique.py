from lab_python_fp.gen_random import gen_random

class Unique:
    """Итератор, оставляющий только уникальные значения."""
    def __init__(self, data, **kwargs):
        self.used_elements = set() 
        self.data = data
        self.index = 0
        self.ignore_case = kwargs.get('ignore_case') 

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.index >= len(self.data):
                raise StopIteration
            else:
                current = self.data[self.index] 
                if ((self.ignore_case == True)and(type(current)==str)):
                    current = current.lower()
                self.index = self.index + 1
                if current not in self.used_elements:
                    self.used_elements.add(current)
                    return current

def main():
    print('Задание 3:')
    print('Пример 1:')
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    for i in Unique(data):
        print(i)

    print('Пример 2:')
    data = gen_random(6, 1, 3)
    for i in Unique(data):
        print(i) 

    print('Пример 3:')
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    for i in Unique(data):
        print(i) 

    print('Пример 4:')
    for i in Unique(data, ignore_case = True):
        print(i) 

if __name__ == "__main__":
    main()

