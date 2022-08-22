# ДЗ
# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон

class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.s = x * y

    def __add__(self, other):
        return self.s + other.s

    def __sub__(self, other):
        return self.s - other.s

    def __eq__(self, other):
        return self.s == other.s

    def __nq__(self, other):
        return self.s != other.s

    def __gt__(self, other):
        return self.s > other.s

    def __lt__(self, other):
        return self.s < other.s

    def __len__(self, other):
        return (self.s + other.s) * 2


rect1 = Rectangle(5, 10)
rect2 = Rectangle(5, 9)
print(rect1 > rect2)
print(rect1 + rect2)
print(rect1 - rect2)


# Task2
# создать класс Human (name, age)
# создать два класса Prince и Cinderella:
# у золушки должно быть имя возраст и размер ноги
# у принца имя, возраст и размер найденной туфельки, так же должен быть метод который принимает лист золушек и ищет ту самую
#
# в классе золушки должна быть переменная count которая будет считать сколько экземпляров класса золушка было создано
# и метод класса который будет показывать это количество
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):
    def __init__(self, name, age, size):
        super().__init__(name, age)
        self.size = size

    def __str__(self):
        return str(self.__dict__)


class Prince(Human):
    def __init__(self, name, age, shoe_size):
        super().__init__(name, age)
        self.shoe_size = shoe_size

    def find_cind(self, cinderellas: list[Cinderella]):
        count = 0
        for cinderella in cinderellas:
            count += 1
            if cinderella.size == self.shoe_size:
                print(cinderella)
                break
        print(f'Count of cinderellas {count}')


cinderellas: list[Cinderella] = [
    Cinderella('Lilya', 18, 37),
    Cinderella('Ira', 20, 39),
    Cinderella('Luda', 25, 40),
    Cinderella('Alina', 23, 35)
]

prince = Prince('Oleh', 18, 35)
prince.find_cind(cinderellas)
# Task3
# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
# Приклад:
#
# Main.add(Magazine('Magazine1'))
# Main.add(Book('Book1'))
# Main.add(Magazine('Magazine3'))
# Main.add(Magazine('Magazine2'))
# Main.add(Book('Book2'))
#
# Main.show_all_magazines()
# print('-' * 40)
# Main.show_all_books()
#
# для
# перевірки
# ксассів
# використовуємо
# метод
# isinstance, приклад:
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False
from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


class Book:
    def __init__(self, name):
        self._name = name

    def print(self):
        print(self._name)


class Magazine:
    def __init__(self, name):
        self._name = name

    def print(self):
        print(self._name)


class Main:
    printable_list: list[Printable] = []

    @classmethod
    def add(cls, other_item: Printable):
        if isinstance(other_item, Book) or isinstance(other_item, Magazine):
            cls.printable_list.append(other_item)

    @classmethod
    def show_all_magazines(cls):
        for item in cls.printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        for item in cls.printable_list:
            if isinstance(item, Book):
                item.print()


Main.add(Magazine('mag1'))
Main.add(Magazine('mag2'))
Main.add(Magazine('mag3'))

Main.add(Book('Jojo'))
Main.add(Book('Joro'))
Main.add(Book('Jobo'))

Main.show_all_magazines()
print('-' * 20)
Main.show_all_books()
