#!/usr/bin/env python3.4


""" This is a small utility to mesure a time for reading data by user"""

import time

print("Консольная утилита для анализа времени оценки информации полученной с экрана \n")


inp=input("Введите дату рождения: " )


start = time.time()
inp1=input("Ваша дата рождения верна?(да/нет) ")


if inp1=="да":
     print('все отлично \n')
     end = time.time()
     print(end-start)

if inp1=="нет":
     print('проверьте её \n')
     end = time.time()
     print(end-start)





