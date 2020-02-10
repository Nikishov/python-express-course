import random


#Экспресс курс по языку Python. Выберите от 1 до 10, чтобы проверить соответствующее цифре задание

print ("Выберите от 1 до 10, чтобы проверить соответствующее цифре задание")


#Задание 1
part = int(input())
if part == 1:
    print ("Привет, мир!!!")

#-------------------------------------------------------------#
#-------------------------------------------------------------#
#-------------------------------------------------------------#

#Задание 2
if part == 2:
    not_a_number = None
    integer = 2
    f_loat = 4.5
    Stroka = "47.5"
    Spisok = [1, 2, 3, 4, 5]
    Kortegh = (1, 2, 3, 4, 5)
    slovar = {'b': 1, 'c': 2}
    Mnoghestvo = set("Это множество")
    print(type(not_a_number), " ", type(integer), " ", type(f_loat), " ", type(Stroka), " ",type(Spisok), " ", type(Kortegh), " ", type(slovar), " ", type(Mnoghestvo))
    print("Из int во float -", float(integer), "и наоборот -", int(f_loat))
    print("Из string во float -", float(Stroka), "и наоборот -", str(f_loat))
    print ("Размер строки: ", len(Stroka), " Размер списка: ", len(Spisok), " Размер кортежа: ", len(Kortegh), " Размер словаря: ", len(slovar), " Размер множества: ", len(Mnoghestvo))
    print("Первый и последний элементы строки: ", Stroka[0::3], ", списка: ", Spisok[::4], ", кортежа", Kortegh[::4])
    print("Кроме первого и последнего в строке: ", Stroka[1:3:1], ", списка: ", Spisok[1:4:1], ", кортежа", Kortegh[1:4:1])
    print("Значение ключа b равно", slovar['b'])

#-------------------------------------------------------------#
#-------------------------------------------------------------#
#-------------------------------------------------------------#

#Задание 3
if part == 3:
    istina = True
    logh = False
    print(type(istina), type(logh))
    print(logh and istina, logh or istina, not logh, not istina)
    a = 3
    b = 7
    print(a == b, "---", a != b, "---", a < b, "---", a > b, "---", a >= b, "---", a <= b)
    print("Результат действия сложения:", a + b, "--- вычитания:", a - b, "--- умножения:", a * b, "--- деления:",  a / b, "--- возведения в степень:", a ** b, "--- деления по модулю:", a % b, "--- целочисленного деления:", a // b)

#-------------------------------------------------------------#
#-------------------------------------------------------------#
#-------------------------------------------------------------#

#Задание 4
if part == 4:
    print ("Введите число, которое находится в интервале [-100; 100]")
    number = int(input())
    if number > 100 or number < -100:
        print ("Число не входит в интервал!!!")
    elif number < -50:
        print ("Число меньше -50")
    elif number == -50:
        print ("Число равно -50")
    elif number < 0 and number > -50:
        print ("Число меньше 0, но больше -50")
    elif number > 0 and number < 50:
        print ("Число больше 0, но меньше 50")
    elif number == 50:
        print ("Число равно 50")
    elif number > 50:
        print ("Число больше 50")

#-------------------------------------------------------------#
#-------------------------------------------------------------#
#-------------------------------------------------------------#

#Задание 5
if part == 5:
    arr_for = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Вывод значений от 1 до 10 в цикле for")
    for i in arr_for:
        print(i, end = " ")
    print (" ")
    arr_while = 1
    print("Вывод значений от 1 до 10 в цикле while")
    while arr_while <= 10:
        print(arr_while, end = " ")
        arr_while = arr_while + 1
    print(" ")
    print("Вывод ФИО")
    FIO = "Никишов Даниил Андреевич"
    for j in FIO:
        print(j, end = " ")

    print(" ")
    print("Список друзей")
    friend1 = "friend1"
    friend2 = "friend2"
    friend3 = "friend3"
    data1 = ["22","12","2000"]
    data2 = ["04","05","2000"]
    data3 = ["11","09","2000"]

    date_of_birth = {friend1: data1, friend2: data2, friend3: data3}

    for key, value in date_of_birth.items():
        if date_of_birth[key][1] != "06" and date_of_birth[key][1] != "07" and date_of_birth[key][1] != "08" and date_of_birth[key][1] != "09" and date_of_birth[key][1] != "10" and date_of_birth[key][1] != "11":
            print(key, value)

#-------------------------------------------------------------#
#-------------------------------------------------------------#
#-------------------------------------------------------------#

#Задание 6
if part == 6:
    def privetstvie():
        print("Hello world")
    privetstvie()
    def my_name(name):
        print(name)
    my_name("Daniil")
    def Discriminant(a, b, c):
        D = b*b - 4*a*c
        print(D)
    Discriminant(2, 3, 5)
    def name_and_age():
        print("Впишите имя и возраст")
        name = input()
        age = input()
        print("Вы", name, ",ваш возраст:", age )
    name_and_age()
    def alphavit(number):
        alp='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        if number <= len(alp):
            p = alp[number-1]
            return p
            
        elif number > 33:
            print("Error")
    print(alphavit(27))

#-------------------------------------------------------------#
#-------------------------------------------------------------#
#-------------------------------------------------------------#

#Задание 7
if part == 7:
    my_FIO = "Никишов Даниил Андреевич"
    print(len(my_FIO))
    print("Никишов " + "Даниил " + "Андреевич")
    print(my_FIO[8:15])
    print(my_FIO.upper())
    print(my_FIO.split(" "))
    
#-------------------------------------------------------------#
#-------------------------------------------------------------#
#-------------------------------------------------------------#

#Задание 8
if part == 8:
    not_a_number = None
    my_list = [not_a_number, 7, 6.1, "Никишов Даниил Андреевич", [1, 2, 3], (1, 2, 3), {1 : "1", 2 : "2", 3 : "3"}]
    for i in my_list:
        print(type(i))
    my_list.pop()
    t = list(my_list[3])
    print(t)
    t = my_list[3]
    print(t)
    for j in range(len(t)):
        print(t[j], j)
    t = list(my_list[3])
    print(t.count('а'))
    
#-------------------------------------------------------------#
#-------------------------------------------------------------#
#-------------------------------------------------------------#

#Задание 9
if part == 9:
    spisok = []
    for i in range (100):
        i = random.randint(1, 100)
        print(i)

#-------------------------------------------------------------#
#-------------------------------------------------------------#
#-------------------------------------------------------------#

#Задание 10
if part == 10:
    def exeption(a, b):
        c = a / b
        try:
            c = a / 0
        except ZeroDivisionError:
            c = 0
        print(c)
    exeption(3, 3)