# Урок 4 Домашнее задание - Easy
#
#
import re
#описание проверочных выражений
Name_rule = '^[A-ZА-Я][a-zа-я]+'
Surename_rule = '^[A-ZА-Я][a-zа-я-]+'
email_rule = '[a-z_0-9]+@[a-zA-Z-]+\.(ru|org|com)'
pattern=(Name_rule, Surename_rule, email_rule)
#Создание списков с вопросами и значениями Имени, Фамилии и e-mail
Questions = ['ваше имя ',' вашу фамилию ','ваш E-mail адрес ']
Person = ['name', 'surename', 'email']
# цикличский ввод имени фамилии и e-mail
i = 0
while i < 3:
    Person[i] = input('Введите '+ Questions[i])
    if re.match(pattern[i],Person[i]):
# если введенные данные совпадают с проверочным выражением то переходим к следующему значениию
        i = i+1
    else:
        print('Вы ввели неправильное значение')
print(Person)