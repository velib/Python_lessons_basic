# ФИО Волков Евгений

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

# ответ: Но не заработало
fruits = ["яблоко", "банан", "киви", "арбузики"]
space = ' ' #просто пробел
l = 0 # кол-во букв в наиболее длинном слове
i = 0
while len(fruits) > i:
  if len(fruits[i])>l:
    l=len(fruits[i])
  i += 1

i = 0
while len(fruits) > i:
  spaces = space * (l - len(fruits[i]))
  print('{}.{}{}'.format(i+1, spaces, fruits[i])
  i += 1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

spisok1 = ['12', '14', 'hello', 'яблоко']
spisok2 = ['10', '16', 'hello', 'ананас']
for word1 in spisok1:
  for word2 in spisok2:
    if spisok1[word1] == spisok2[word2]:
      spisok1[word1] = []
 

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
        
        spisok = ['12', '14', '3', '0', '10']
print('Old list', spisok)
i = 0
while len(spisok) > i:
  if spisok[i] % 2 == 0):
      spisok[i] = spisok[i] / 4
  else
      spisok[i] = spisok[i] * 2
  i += 1

print('new list', spisok)
