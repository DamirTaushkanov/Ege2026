#Ex2 Сопоставление таблиц истиности
"""
Алгоритм:
1)Пишем функцию для составлния таблицы
2)Сопотавляем таблицы из задания и нашу
"""
def F(x,y,w,z):
    return (x<=y)and w or z

def main():
    print("X Y W Z| F")
    for x in (0, 1):
        for y in (0, 1):
            for z in (0, 1):
                for w in (0, 1):
                    if F(x, y, z, w):
                        print(x, y, z, w, F(x, y, z, w))

if __name__=='__main__':
    main()