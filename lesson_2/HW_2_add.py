# створити декоратор який буде рахувати кількість запущених функцій продекорованих цим декоратором
def make_decorator():
    count = 1

    def launch(func):
        def inner_launch(*args, **kwargs):
            nonlocal count
            func(*args, **kwargs)
            print(count)
            print('-' * 10)
            count += 1

        return inner_launch

    return launch


decor = make_decorator()


@decor
def func1():
    print('func1')


@decor
def func2():
    print('func2')


func2()
func1()
func1()
func2()
func2()
func1()


# вивести послідовність Фібоначі, кількість вказана в знінній,
#   наприклад: x = 10 -> 1 1 2 3 5 8 13 21 34 55
#   (число з послідовності - це сума попередніх двох чисел)
#
def fib(num):
    a = 0
    b = 1
    if num < 0:
        print('Input correct value')
    elif num == 0:
        return 0
    elif num == 1:
        return b
    else:
        for i in range(1, num):
            c = a + b
            a = b
            b = c
        return b


print('*' * 10)
print(fib(10))


# порахувати кількість парних і непарних цифр числа,
#   наприклад: х = 225688 -> п = 5, н = 1;
#          х = 33294 -> п = 2, н = 3
def even_or_odd(num):
    even = 0
    odd = 0
    res = list(map(int, str(num)))
    for i in res:
        if i % 2 == 0:
            even += 1
        elif i % 2 == 1:
            odd += 1
    print('Even:' + str(even), 'Odd:' + str(odd))
    return even, odd


print(even_or_odd(225688))


# прога, що виводить кількість кожного символа з введеної строки,
# наприклад:
# st = 'as 23 fdfdg544' #введена строка
#
# 'a' -> 1  #вивело в консолі
# 's' -> 1
# ' ' -> 2
# '2' -> 1
# '3' -> 1
# 'f' -> 2
# 'd' -> 2
# 'g' -> 1
# '5' -> 1
# '4' -> 2
