def convert(num):
    res = []
    while num:
        res.append(num%9)
        num //= 9
    return res[::-1]

res = []
for N in range(1,100):
    R = convert(N)
    if R[0] == 7:
        while 6 in R:
            R[R.index(6)] = 3
        while 3 in R != -1:
            R[R.index(3)] = 6
        R = [34] + R
    else:
        R.append(45)
        R[0] = 3
    Rstr = ""
    for num in R:
        Rstr += str(num)
    res.append(int(Rstr, 9))
    print(f"{int(Rstr, 9)} {N}")
print(sorted(res))