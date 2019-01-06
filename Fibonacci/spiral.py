from turtle import Turtle
from tkinter import messagebox
import time

def Spiral():
    t = Turtle()
    a = 17

    def fib(n1):
        liste = []
        def _fib(n):
            a,b = 1,1
            for i in range(n-1):
                a,b = b,a+b
            return a

        for i in range(1,n1):
            liste.append(_fib(i))
        return liste

    fibo_dizi = fib(a)
    print(fibo_dizi)

    def kare_ciz(liste_uz):  
        for i in range(4):
            t.forward(liste_uz)
            t.right(90)

    liste_uzunluğu = len(fibo_dizi)

    genis = 1                   
    t.penup()
    t.goto(50,50)                  
    t.pendown()

    for i in range(liste_uzunluğu):
        kare_ciz(genis*fibo_dizi[i])
        t.penup()                        
        t.forward(genis*fibo_dizi[i])
        t.right(90)
        t.forward(genis*fibo_dizi[i])
        t.pendown()
        
    t.penup()
    t.goto(50,50)       
    t.setheading(0)   
    t.pencolor('blue')
    t.pensize(2)
    t.pendown()

    for i in range(liste_uzunluğu):
        t.circle(-genis*fibo_dizi[i],90)
    time.sleep(3)
    

if __name__ == '__main__':
    Spiral()
