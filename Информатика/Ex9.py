#Ex9 Поиск нужно строчки в exel
"""
Алгоритм:
1)копируем таблицу в txt файл
2)перебираем построчно весь файл и ищем нужную строку по условию
"""
f = open("9_21592.txt")
number = 0
for i in f:
    number += 1
    tworepeat = []
    nonrepeat = []
    num_list = i.split("	")
    for num in num_list:
        if num_list.count(num) == 2:
            tworepeat.append(int(num))
        elif num_list.count(num) == 1:
            nonrepeat.append(int(num))
    if len(tworepeat) == 6 and len(nonrepeat) == 2 and ((max(tworepeat)-min(tworepeat))**2)>((nonrepeat[0]**2)+(nonrepeat[1]**2)):
        print(f"{number} {i}")
