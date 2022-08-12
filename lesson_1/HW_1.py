# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.
st = 'as 23 fdfdg544'
print(','.join(i for i in st if i.isdigit()))
# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі
# #################################################################################
print(','.join(''.join(i if i.isdigit() else ' ' for i in st).split()))

# list comprehension
#
# 1)є строка:
#greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
def greet():
    greeting = 'Hello, world'
    print([i.upper() for i in greeting])
greet()
# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
print([i**2 for i in range(0,50) if i % 2 == 1])
# function
#
# - створити функцію яка виводить ліст
def lst(lt):
    for i in lt:
        print(i)

lst([1,2,3,4,5])
# - створити функцію яка приймає три числа та виводить та повертає найбільше.
def numList(num):
    return print(max(num))

numList([123,-3123,54637])
# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def numList2(*args):
    print(max(*args))
    return print(min(*args))

numList2([123,4235,-42482])
# - створити функцію яка повертає найбільше число з ліста
def maxList(lt):
    return print(max(lt))

maxList([123,334234,1441,-4234])
# - створити функцію яка повертає найменьше число з ліста
def minList():
    lt = [[1232,-365,4237427]]
    return print(min(lt))
minList()
# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
def sumList(lt):
    total = 0
    for i in lt:
        total += i

    return print(total)

sumList([1,2,3,4,5])
# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
def avgList(lt):
    avg = sum(lt)/len(lt)
    return print(avg)

avgList([1,2,3,4,5])

################################################################################################
# 1)Дан list:
list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
print(min(list))
#   - видалити усі дублікати
def duplicate():
    list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
    list = set(list)
    print(list)
duplicate()
#   - замінити кожне 4-те значення на 'X'
list2 = [22, 3,5,2,8,2,-23, 8,23,5]
def swap():
    list2 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
    print(['X' if (i+1)% 4 == 0 else val for i,val in enumerate(list2)])
swap()
# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def square():
    n = 10
    for i in range(n):
     if i == 0 or i == n - 1:
        print('*' * n)
     else:
         print('*' + ' ' * (n - 2) + ' ' + '*')

square()
# 3) вывести табличку множення за допомогою цикла while
def multiply():
    i = 1
    while i <= 9:
        l = 1
        while l <= 9:
             mult = i * l
             l += 1
             print(f'{mult:3}', end='')
        i += 1
        print()
multiply()
# 4) переробити це завдання під меню
while True:
    print('1. minList')
    print('2. duplicate')
    print('3. swap')
    print('4. square')
    print('5. multiply')
    print('6. exit')

    choice = input('Click on num to choose: ')

    if choice == '1':
        minList()
    elif choice == '2':
        duplicate()
    elif choice == '3':
        swap()
    elif choice == '4':
        square()
    elif choice == '5':
        multiply()
    elif choice == '6':
        break

