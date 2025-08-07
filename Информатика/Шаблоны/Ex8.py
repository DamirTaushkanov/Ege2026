#Ex8 Комбинаторика, поиск нужной последовательности
"""
1. Составляем алфаит и сортируем его
2. C помощью itertools перебираем все возможные последовательности
3. Если символы могут повторяться то функция product, если только перестановки то функция permutation 
4. Среди этих последовательностей ищем подходящие по условию
"""
from itertools import product, repeat

def valid(number, str):
    res = False
    if number%2==0 and str[0] not in "АГ" and str.count("Р")>=2:
        res = True
    return res

def main():
    alh = "АЛГОРИТМ"

    number = 0
    for str in  product(sorted(alh), repeat=5):
        number += 1

        if valid(number, str):
            print(f"{number} {str}")
            break

if __name__ == '__main__':
    main()