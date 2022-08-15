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
# def fib(num):


# fib(10)
# порахувати кількість парних і непарних цифр числа,
#   наприклад: х = 225688 -> п = 5, н = 1;
#          х = 33294 -> п = 2, н = 3
