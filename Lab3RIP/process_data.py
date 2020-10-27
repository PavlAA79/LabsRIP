import json
import sys
from lab_python_fp.gen_random import gen_random
from lab_python_fp.cm_timer import cm_timer_1
from lab_python_fp.print_result import print_result
from lab_python_fp.Unique import Unique

path = 'C:\\Users\\Настя\\source\\repos\\LabsRIP\\Lab3RIP\\data_light1.json'

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария
with open(path,encoding='utf-8') as f:
    data = json.load(f)


# Сортировка списка профессий без повторений
#(строки в разном регистре считаются равными)
@print_result
def f1(arg):
    result11 = []
    for i in arg:
        result11.append(i['job-name'])
    result12 = list(sorted(Unique(result11,ignore_case = True)))
    return result12
    
# Вывод входного массива только с теми элементами,
# которые начинаются со слова “программист”. 
@print_result
def f2(arg):
    result2 = list(filter(lambda i: i.startswith('программист'), arg))
    #result2 = list(filter(lambda i:'программист' in i, arg))
    return result2


# Добавление к каждому элементу массива строки “с опытом Python” 
@print_result
def f3(arg):
    result3 = list(map(lambda x: x+' с опытом Python', arg))
    return result3

#Генерирование для каждой специальности зарплаты от 100 000 до 200 000 рублей 
#и присоединение её к названию специальности
@print_result
def f4(arg):
    salary = list(map(lambda x:'зарплата '+str(x)+' руб.' , gen_random(len(arg), 100000, 200000)))
    result4 = list(zip(arg, salary))
    return result4


def main():
    print('Задание 7:')
    with cm_timer_1(): 
        try:
            f4(f3(f2(f1(data))))
        except:
            pass

if __name__ == "__main__":
    main()
