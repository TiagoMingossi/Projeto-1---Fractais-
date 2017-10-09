# -*- coding: utf-8 -*-
'''
Created on Fri Sep 15 10:16:51 2017

@author: Jorge

'''
import turtle

turtle.hideturtle()
turtle.pensize(8)

Exemplos=input("Exemplos de codigos: o - oo - oo - o | o - - ooo - - o | oo - o - - o - - o - oo")
entrada=input("Digite aqui o seu codigo: ").split(" ")
angulo=int(input("Digite aqui um angulo de inclinação (graus): "))
cor=input("Digite aqui uma cor (ingles): ")

contador=0
maximo_contador=0
codigo=0

for i in entrada:
    if i == "-":
        maximo_contador = maximo_contador + 1
    if i == "o":
        codigo = codigo + 10
    if i == "oo":
        codigo = codigo + 20
    if i == "ooo":
        codigo = codigo + 30
    if i == "oooo":
        codigo = codigo + 40
    if i == "ooooo":
        codigo = codigo + 50

turtle.pencolor(cor)        
turtle.left(90)
turtle.up()
turtle.backward(150)
turtle.down()
turtle.forward(codigo)

def arvore(codigo,contador):
    tamanho=turtle.pensize()
    turtle.pensize(tamanho*2/3)
    
    codigo = codigo - 5
    turtle.right(angulo)
    turtle.forward(codigo)
     
    if contador<maximo_contador:
        arvore(codigo,contador+1)
        
    turtle.pencolor(cor)
    turtle.up()
    turtle.backward(codigo)
    turtle.down()
    turtle.left(angulo*2)
    turtle.forward(codigo)
    
    if contador<maximo_contador:
        arvore(codigo,contador+1)
        
    turtle.pencolor(cor)
    turtle.up()    
    turtle.backward(codigo)
    turtle.down()
    turtle.right(angulo)   
    turtle.pensize(tamanho)
    
arvore(codigo,contador)
turtle.speed("fastest")
turtle.done()