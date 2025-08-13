def main():
    res = 0

    for n in range(4,10000):
        s = "4" + "2" * n

        while "42" in s or "822" in s or "222" in s:
            if "42" in s:
                s = s.replace("42", "2", 1)
            if "822" in s:
                s = s.replace("822", "24", 1)
            if "222" in s:
                s = s.replace("222", "8", 1)
        num = [int(num) for num in s]
        if res<sum(num):
            res = sum(num)
    print(res)
if __name__=='__main__':
    main()