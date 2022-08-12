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