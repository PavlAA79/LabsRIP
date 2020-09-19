import math
print('Павловская Анастасия ИУ5-51Б')

print('ax^4+bx^2+c=0')
a = 0
b = 0
c = 0
x1 = 0
x2 = 0
discriminant = 0
cycle = 1

while cycle == 1:
    print('Введите коэффициент a:')
    try:
        a = float(input())
    except ValueError:
        continue
    else:
        break

while cycle == 1:
    print('Введите коэффициент b:')
    try:
        b = float(input())
    except ValueError:
        continue
    else:
        break

while cycle == 1:
    print('Введите коэффициент c:')
    try:
        c = float(input())
    except ValueError:
        continue
    else:
        break

if a == 0 and b == 0 and c == 0: 
    print('0 = 0')

if a == 0 and b == 0 and c != 0:  
    print('Нет корней')

if a == 0 and b != 0 and c != 0:
    if (b > 0 and c > 0) or (b < 0 and c < 0):
        print('Нет корней')
    else:
        x1 = math.sqrt((-c)/b)
        print('Два корня: x1 = ',x1, ', x2 = ', -x1)

if a != 0 and b == 0 and c != 0:
    if (a > 0 and c > 0) or (a < 0 and c < 0):
        print('Нет корней')
    else:
        x1 = math.sqrt(math.sqrt((-c)/a))
        print('Два корня: x1 = ',x1, ', x2 = ', -x1)

if a != 0 and b == 0 and c == 0:
     print('Один корень: x = 0')

if a == 0 and b != 0 and c == 0:
     print('Один корень: x = 0')

if a != 0 and b != 0 and c != 0:
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        print('Нет корней')
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant))/(2*a)
        x2 = (-b - math.sqrt(discriminant))/(2*a)
        if x1 > 0 and x2 > 0:
            print('Четыре корня: x1 = ',math.sqrt(x1), ', x2 = ', -math.sqrt(x1))
            print('x3 = ', math.sqrt(x2), ', x4 = ', -math.sqrt(x2))
        if x1 > 0 and x2 < 0:
            print('Два корня: x1 = ',math.sqrt(x1), ', x2 = ', -math.sqrt(x1)) 
        if x1 < 0 and x2 > 0:
            print('Два корня: x1 = ',math.sqrt(x2), ', x2 = ', -math.sqrt(x2))
        if x1 < 0 and x2 < 0:
            print('Нет корней')
    if discriminant == 0:
        x1 = (-b/2*a)
        if x1 > 0:
            print('Два корня: x1 = ',math.sqrt(x1), ', x2 = ', -math.sqrt(x1))
        if x1 < 0:
            print('Нет корней')
