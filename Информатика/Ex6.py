#Ex6 Черепашка
"""
Алгоритм:
1)инициализируем черепаху
2)прописывае все движегния черпахи
3)отрисовываем сетку точек
4)подсчтываем то что требуют
"""
from turtle import *

def init_turtle():
    screensize(2000, 2000)
    left(90)
    tracer(0)

def field(k):
    penup()
    for x in range(-70,70):
        for y in range(-70,70):
            goto(x*k, y*k)
            dot(3,"BLACK")

def main():
    init_turtle()
    k = 10

    for i in range(5):
        fd(37*k)
        rt(90)
        fd(44*k)
        rt(90)

    penup()

    bk(18*k)
    rt(90)
    fd(29*k)
    lt(90)

    pendown()

    for i in range(5):
        fd(31*k)
        rt(90)
        fd(35*k)
        rt(90)

    field(k)

    exitonclick()

if __name__ == '__main__':
    main()