# написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
# - первый записывает в эту переменную запись
# - второй возвращает все записи
#
# запишите 5 тудушек
# и выведете все
# 2) протипизировать первое задание
def notebook():
    todo_list: list[str] = []

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list.append(todo)

    def get_all_todos() -> list[str]:
        nonlocal todo_list
        return todo_list

    return add_todo, get_all_todos


add, get = notebook()
add('learn')
add('work')
add('workout')
add('eat')
add('sleep')
print(get())


# 3) создать функцию которая будет возвращать сумму разрядов числа в виде строки (тоже с типизацией)
#
# Пример:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'
def expanded_form(num: int) -> str:
    st = str(num)
    zero_count = len(st) - 1
    print([v + '0' * (zero_count - i) for i, v in enumerate(st) if v != '0'])


expanded_form(555)


# создать декоратор который будет считать сколько раз была запущена функция и будет выводит это значение после
# каждого запуска функции

def decor(func):
    count = 1

    def inner(*args, **kwargs):
        nonlocal count
        print('*' * 10)
        print(f'{count=}')
        func(*args, **kwargs)
        print('*' * 10)
        count += 1

    return inner


@decor
def func1():
    print("func1")


func1()
func1()
func1()
