def find_del(num):
    res = []  
    for i in range(1, int(num**0.5)+1):
        if num%i==0:
            res.append(i)
    return res

def find(num):
    res = 0
    list_del = find_del(num)
    for i in list_del:
        if is_prime(i) and one_six(i) and is_prime(num/i) and one_six(num/i):
            print(f"{num} - Num1 {i} Num2 {i}")
            res = 1
    return res

def one_six(num):
    res = False
    num = str(num)
    if num.count('6') == 1:
        res = True
    return res

def is_prime(num):
    res = False
    if len(find_del(num))==1:
        res = True
    return res

def main():
    num = 6086055
    flag = 0
    while flag!=5:
        flag += find(num)
        num += 1

if __name__ == '__main__':
    main()