# Домашнее задание 
# def __sub__(self, other)  # вычитание дробей
# def __mul__(self, other)  # умножение дробей
#

class Alpha:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __sub__(self, other):
        return Alpha(self.num1 * other.num2 - self.num2 * other.num1,   
                     self.num2 * other.num2)

    def __str__(self):
        return f"{self.num1}/{self.num2}"

n1 = Alpha(6, 8)
n2 = Alpha(8, 6)
print(n1 - n2)  

class Omega:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __mul__(self, other):
        return Alpha(self.num1 * other.num1, self.num2 * other.num2)    
    
    def __str__(self):
        return f'{self.num1}/{self.num2}'

o1 = Omega(2, 3)
o2 = Omega(3, 4)
print(o1 * o2)   


# Магические методы в Python
# Повторим классы. Рассмотрим готовый класс дата и время
from datetime import datetime
dt = datetime.now()  # Запросить текущую дату и время
print(dt)
# strftime = string formatted time
print(
    dt.year,
    '-',
    dt.month,
    dt.day
)
print(
    dt.strftime('%d.%m.%Y %H:%M'),
)
print(
    dt.strftime('%d %B %Y %H:%M'),
)

# https://docs.python.org/3.13/library/datetime.html#strftime-and-strptime-behavior
# Табличка всех доступных спецсимволов для форматирования строки

# strptime = string parsed time
dt = datetime.strptime(  # Бросает исключение, если что-то идет не так
    '2 January, 2021 time: 12:45',
    '%d %B, %Y time: %H:%M'
)
print(dt)

# strptime - статическая функция. Почему? Что это такое?
# Как написать свою статическую функцию?


# dtstart = 11 апреля 1955
# seconds_in_day = 88775.24409
# Почему земные сутки имеют круглое число секунд?
# sols_in_mars_year = 668.5991

class Mars_Time(datetime):  # Унаследовали datetime
    dtstart           = datetime(1955, 4, 11)
    seconds_in_day    = 88775.24409
    sols_in_mars_year = 668.5991  # mars days in mars year

    @property
    def mars_year(self):
        return (self.year - self.dtstart.year) / 2  # надо по-хорошему, брать секунды и делить на секунды!
        # return (self.year - 1955) / 2  # Упрощенно

    # Магический метод, вызывающийся при print() и str()
    def __str__(self):
        return 'Земное время: ' + super().__str__() + '\nМарсианское время: ' + str(self.mars_year) + ' года от начала времен'

mtime = Mars_Time(1999, 1, 25)  # Чтобы создать объект любого класса в питоне, надо
                     # создать переменную и присвоить ей результат вызова этого класса
                     # подобно функции (так вызывается конструктор)
                     # js: let dt = new Date(1999, 0, 25)
# Также можно было вызывать Mars_Time.now()
print(mtime)
print(mtime.seconds_in_day)
print(mtime.hour)
print(mtime.year)
print(mtime.mars_year) #())


# Магические методы сравнения на неравенство

class Human:
    def __init__(self, name, height):
        self.__name = name
        self.__height = height


#object.__eq__(self, other)  # == equal
#object.__ne__(self, other)  # != not equal
#   def __lt__(self, other):  # <  less than
    def __gt__(self, other):  # >  greater than
        return self.__height > other.__height

#   def __le__(self, other):  # <= less or equal
    def __ge__(self, other):  # >= greater or equal
        return self.__height >= other.__height


h1 = Human('Вася', 185)
h2 = Human('Ася', 163)
print(h1 <= h2)


# Напишите класс "обыкновенная дробь" (с числителем и знаменателем)
# и сделайте сравнение двух дробей не только на равно, но и на
# больше, меньше





class Drob:
    def __init__(self, chisl, znam):
        self.chisl = chisl # числитель
        self.znam = znam # знаменатель

    def  __eq__(self, other):  # other - другой
        #  ch1        ch2
        # ------  -  ------ = ch1 * zn2 - zn1 * ch2 == 0
        #  zn1        zn2
        # return ch1 * zn2 - zn1 * ch2 == 0
        return self.chisl * other.znam - self.znam * other.chisl == 0

    def __add__(self, other):
        return Drob(
            self.chisl * other.znam + self.znam * other.chisl,
            other.znam * self.znam
        )

    def __str__(self):
        return str(self.chisl) + '/' + str(self.znam)

d1 = Drob(1, 2)  # 1/2   =  3/6
d2 = Drob(2, 3)  # 2/3   =  4/6
d3 = Drob(2, 4)
print(d1 == d3)
print(d1 == d2)
print(d1 + d2)   # 3/6 + 4/6 = 7/6
# Кому не лень, сделать с сокращением дроби. (Сами, не ища алгоритм!)


    
