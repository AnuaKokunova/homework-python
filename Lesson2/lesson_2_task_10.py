# -*- coding: utf-8 -*-

x = int(input("Введите размер вклада : "))
y = int(input("Введите срок :"))

def bank(x,y) : 
    return x*((1.1)**y)
  
print (bank(x,y))