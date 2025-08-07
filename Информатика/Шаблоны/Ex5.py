#Ex5 Конвертация числа в другую систему и валидация
"""
Алгоритм:
1)Определяем систему счесления
2)Если основание 2 то просто конвертируем через bin, 
если другая то пишем функцию конвертации
3)Подаем на вход валидации числа от 1 до примерно 1000
4)Выбераем ответ какой нужен в задании
"""
def convert(num, n):
    res = []
    while num:
        res.append(num%n)
        num //= n
    return res[::-1]

def valid(R):
    if R[0] == 7:
        while 6 in R:
            R[R.index(6)] = 3
        while 3 in R:
            R[R.index(3)] = 6
    else:
        R.append(45)
        R[0] = 3
    return R

def list_to_str(R):
    Rstr = ""
    for num in R:
        Rstr += str(num)
    return Rstr

def main():
    res = [0,0]
    for N in range(1,1000):
        R = convert(N, 9)
        R = valid(R)
        if int(list_to_str(R), 9) < 2876:
            print(f"{int(list_to_str(R), 9)} {N}")
            if res[0]<=int(list_to_str(R), 9):
                res = [int(list_to_str(R), 9), N]
    print(res)

if __name__=='__main__':
    main()