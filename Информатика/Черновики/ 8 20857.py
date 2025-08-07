from itertools import product

def main():
    alh = "012345678"
    number = 0
    for num in product(alh, repeat=6):
        if num[0] in "12345678":
            number += 1
            if (num[0] in '02468' or num[1] in '02468') and\
                (num[1] in '02468' or num[2] in '02468') and\
                    (num[2] in '02468' or num[3] in '02468') and\
                        (num[3] in '02468' or num[4] in '02468') and\
                        (num[4] in '02468' or num[5] in '02468'):
                if number % 10 == 5:
                    print(f"{number} {num}")
            

if __name__=='__main__':
    main()