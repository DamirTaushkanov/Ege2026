#Ex9 Поиск нужно строчки в exel
"""
Алгоритм:
1)Копируем таблицу в txt файл
2)Перебираем построчно весь файл и ищем нужную строку по условию
"""


def main():
    num_list = [a.strip().split('	') for a in [i for i in open("../Исходники/9_21592.txt")]]
    number = 0
    for num_str in num_list:
        number += 1
        tworepeat = []
        nonrepeat = []
        for num in num_str:
            if not num.isdigit():
                continue
            if num_str.count(num) == 2:
                tworepeat.append(int(num))
            elif num_str.count(num) == 1:
                nonrepeat.append(int(num))
        if len(tworepeat) == 6 and len(nonrepeat) == 2 and ((max(tworepeat)-min(tworepeat))**2)>((nonrepeat[0]**2)+(nonrepeat[1]**2)):
            print(f"{number}: {num_str}")

if __name__ == '__main__':
    main()