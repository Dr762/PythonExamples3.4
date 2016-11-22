#!/usr/bin/env python3.4


""" This is a small utility to mesure a time for reading data by user"""

import time

print("Консольная утилита для анализа времени оценки информации полученной с экрана \n")

start = time.time()
inp=input("Введите дату рождения: " )

end=time.time()
delta=end-start
print(delta)
start1 = time.time()
inp1=input("Ваша дата рождения верна?(да/нет) ")


if inp1=="да":
     print('все отлично \n')
     end1 = time.time()
     delta=end1-start1
     print(delta)

if inp1=="нет":
     print('проверьте её \n')
     end1 = time.time()
     delta = end1-start1
     print(delta)





